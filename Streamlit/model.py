import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from config import Idea, Data, idea_prompt, data_prompt

load_dotenv()

class Model(object):
    def __init__(self) -> None:
        self.llm = ChatGroq(
            temperature=0.8,
            model = "llama-3.1-8b-instant", 
            api_key=os.getenv("grow_api_key")
        )
    
    def generate_content(self, category: str, idea: str):
        sequential_idea_chain = idea_prompt | self.llm.with_structured_output(Idea)
        sequential_data_chain = data_prompt | self.llm.with_structured_output(Data)
        try:
            idea_dict = {"category": category, "idea": idea}
            business_name = sequential_idea_chain.invoke(idea_dict)
            data_dict = {"category": category, "name" : business_name.name}
            response = sequential_data_chain.invoke(data_dict)
            return response
        except:
            return "Error"

if __name__ == "__main__":
    print("Welcome User!")
    idea: str = input("Enter a business idea: ")
    category: str = input("Enter category: ")
    