from pathlib import Path
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from dotenv import load_dotenv
load_dotenv()

# step 1 : Load the data
BASE_DIR = Path(__file__).resolve().parent

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstores = Chroma(collection_name="bfl_policy",
                      embedding_function=embedding_model,
                      persist_directory=BASE_DIR / "bfl_db")


retrieval = vectorstores.as_retriever(search_type="similarity", search_kwargs={"k": 5,
                                                                       
                                                                        })


llm = ChatOpenAI(model="gpt-4o-mini")



prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a Bajaj Finance helpdesk agent.
Answer the customer query using ONLY the policy context below.

STRICT RULES:
- Use ONLY the POLICY CONTEXT provided — never use general knowledge
- If answer is not in context, say exactly:
  "I don't have information on this. Please contact Rahul @ 9152091676."
- Never say "based on general practices" or "typically"
- Never make up numbers, rates, or policies
- Format amounts with Rs and commas (e.g., Rs 8,450)
- "minimum CIBIL score" means the score required for APPROVAL

POLICY CONTEXT:
{context}"""),

    # Chat history goes here — LLM sees previous turns for follow-up context
    # This is SEPARATE from retrieval — ChromaDB never sees this history
    MessagesPlaceholder(variable_name="chat_history"),

    # Only the current query — clean, no history mixed in
    ("human", "{query}"),
])


def format_context(docs):
    if not docs:
        return "I don't have information on this. Please contact Rahul @ 9152091676."
    return "\n".join([f"## {doc.page_content}" for doc in docs])



rag_chain = (
     { "context"     : RunnableLambda(lambda x: x["query"]) | retrieval | format_context,
       "chat_history": RunnableLambda(lambda x: x["chat_history"]),
       "query"       : RunnableLambda(lambda x: x["query"]),}
        | prompt
        | llm
        | StrOutputParser()

)


def rag_answer(query, chat_history=[]):
    return rag_chain.invoke({"query": query, "chat_history": chat_history})


# result = rag_answer("what is interest rate for personal loan?", [])
# print(result)


