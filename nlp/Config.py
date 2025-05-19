from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class Config(BaseModel):
    msg: str = Field("")

prompt = PromptTemplate(
    input_variables=["user_message"],
    template="""
    You are Monkey D. Luffy from one piece
    """,
    validate_template=True
)

