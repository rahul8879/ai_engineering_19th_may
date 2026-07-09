
from pydantic import BaseModel, Field, ValidationError
from typing import Literal, List
from collections import Counter


# Schema for CoT result
class CoTResult(BaseModel):
    category: Literal['Billing','Technical','Feature Request','Churn Risk','Spam','Other']
    urgency: Literal['High', 'Medium', 'Low']
    confidence: int = Field(ge=1, le=10)
    reasoning: str = Field(description='One sentence explanation')
    cot_steps: List[str] = Field(description='3-5 reasoning steps')

# Schema for Tree of Thought branch
class ToTBranch(BaseModel):
    branch_name: str
    reasoning: str
    confidence: int = Field(ge=1, le=10)

# Schema for ToT result
class ToTResult(BaseModel):
    branches: List[ToTBranch] = Field(description='2-3 possible interpretations')
    selected_branch: str
    final_category: Literal['Billing','Technical','Feature Request','Churn Risk','Spam','Other']
    final_urgency: Literal['High', 'Medium', 'Low']
    final_reasoning: str

# Safe fallback
FALLBACK = CoTResult(
    category='Other', urgency='Medium', confidence=1,
    reasoning='Parse failed — routed to general support',
    cot_steps=['Parse failed']
)