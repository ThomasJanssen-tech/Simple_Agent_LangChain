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
question = HumanMessage(content="What's the capital of the moon?")

response = agent.invoke(
    {"messages": [question]}
)

print(response['messages'][1].content)