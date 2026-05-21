# importing libraries
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain.tools import tool
from langchain.agents import create_agent
import streamlit as st
import requests
import os
import urllib.parse

load_dotenv()


# initialize tools

@tool
def fetch_google_results(search_term):
    """Search by using the Google search engine

    Args:
        search_term: Search terms to look for
    """

    headers = {
        "Authorization": "Bearer "+os.getenv("BRIGHTDATA_API_KEY"),
        "Content-Type": "application/json"
    }

    data = {
        "zone": "serp_api8",
        "url": "https://www.google.com/search?q="+urllib.parse.quote(search_term),
        "format": "raw"
    }

    response = requests.post(
        "https://api.brightdata.com/request",
        json=data,
        headers=headers
    )

    #print(response.text)

    return response.text


# initializing model
model = init_chat_model(model="gpt-5-nano")

# initializing agent
agent = create_agent(
    model=model,
    system_prompt="You are a helpful assistant. You have access to the tool fetch_google_results to search on Google",
    tools=[fetch_google_results]
)

# initiate streamlit app

st.set_page_config(page_title="Streamlit Agent", page_icon="🦜")
st.title("🦜 Streamlit Agent")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)


# create the bar where we can type messages
user_question = st.chat_input("How are you?")

# did the user submit a prompt?
if user_question:

    # add the message from the user (prompt) to the screen with streamlit
    with st.chat_message("user"):
        st.markdown(user_question)

        st.session_state.messages.append(HumanMessage(user_question))


    # invoking the agent
    result = agent.invoke({"messages":st.session_state.messages})

    ai_message = result['messages'][-1].content

    # adding the response from the llm to the screen (and chat)
    with st.chat_message("assistant"):
        st.markdown(ai_message)

        st.session_state.messages.append(AIMessage(ai_message))