from dotenv import load_dotenv
from os import getenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
llm = ChatGroq(model=getenv("MODEL_NAME"), api_key=getenv("GROQ_API_KEY"))
history = [SystemMessage(content="You are Caramel AI, you are built by HERE AND NOW AI. You are an English Teacher. You job is to teach English in a friendly. If the user asks you anything apart from English learning, you politely refuse. You should never answer about anything but English language learning")]

print("HERE AND NOW AI's Chatbot! Type quit to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    history.append(HumanMessage(content=user_input))
    response = llm.invoke(history)
    history.append(response)
    print(f"Caramel AI: {response.content}\n")