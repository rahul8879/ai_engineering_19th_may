

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder # what is meesage place holder ??
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory #in built memory in langchain --
from langchain_core.runnables.history import RunnableWithMessageHistory # wait for 15 mint
from langchain_core.messages import HumanMessage, AIMessage,BaseMessage # by default your LLM try --> input --> human or AI meeage
from langchain_core.chat_history import BaseChatMessageHistory
from pydantic import BaseModel, Field
from typing import List
class WindowChatMessageHistory(BaseChatMessageHistory, BaseModel):
    """
    A chat message history that only keeps the last `k` messages.
    
    When the history exceeds k messages, the OLDEST messages
    are silently dropped. This creates a sliding window effect.
    
    Implements BaseChatMessageHistory interface so it works
    seamlessly with RunnableWithMessageHistory.
    """
    messages: List[BaseMessage] = Field(default_factory=list)
    k: int = Field(default=6)  # keep last k messages (= k/2 turns)

    def add_messages(self, messages: List[BaseMessage]) -> None:
        """
        Add new messages, then trim to last k.
        Called automatically by RunnableWithMessageHistory.
        """
        self.messages.extend(messages)
        
        # Trim: keep only the last k messages
        # k=6 means 3 HumanMessages + 3 AIMessages = 3 turns
        if len(self.messages) > self.k:
            dropped = len(self.messages) - self.k
            self.messages = self.messages[-self.k:]
            print(f"  [Window] Dropped {dropped} oldest message(s). Now: {len(self.messages)} messages.")

    def clear(self) -> None:
        """Clear all messages."""
        self.messages = []





