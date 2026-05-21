# importing libraries
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain.tools import tool
from langchain.agents import create_agent

load_dotenv()

# initializing model and agent
model = init_chat_model(model="gpt-5-nano")
agent = create_agent(model=model)


# invoking agent with a question

messages = []

while True:
    user_question = input("Ask a question: ")

    # add user question to messages
    messages.append(HumanMessage(content=user_question))

    # execute the agent with user message
    response = agent.invoke(
        {"messages": messages}
    )

    # print AI answer on the screen
    print("AI says: "+response['messages'][-1].content)

    messages.append(AIMessage(content=response['messages'][-1].content))