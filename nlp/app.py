import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from nlp.Config import Config, prompt

load_dotenv()

class Model(object):
    def __init__(self) -> None:
        self.llm = ChatGroq(
            temperature=0.8,
            model="llama-3.1-8b-instant",
            api_key=os.getenv("groq_api_key")
        )
    
    def chat(self, message: str) -> str:
        sequence_chain = prompt | self.llm.with_structured_output(Config)
        try:
            data = {"user_message": message}
            response = sequence_chain.invoke(data)
            return response
        except:
            error: str = "Error"
            return error

if __name__ == "__main__":
    print("==============Welcome User================")
    model = Model()
    while True:
        msg: str = input("Me: ")
        response = model.chat(message=msg)
        check: str = input("Exit? [y/n]: ")
        print(response.msg)
        if check.lower() == "y":
            break
        