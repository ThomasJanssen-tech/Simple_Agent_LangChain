<h1>Simple Research Chatbot with LangChain</h1>


<h2>Prerequisites</h2>
<ul>
  <li>Python 3.11+</li>
</ul>

<h2>Installation</h2>
<h3>1. Clone the repository:</h3>

```
git clone https://github.com/ThomasJanssen-tech/Chatbot-with-RAG-and-LangChain.git
cd Chatbot-with-RAG-and-LangChain
```

<h3>2. Create a virtual environment</h3>

```
python -m venv venv
```

<h3>3. Activate the virtual environment</h3>

```
venv\Scripts\Activate
(or on Mac): source venv/bin/activate
```

<h3>4. Install libraries</h3>

```
pip install -r requirements.txt
```

<h3>5. Add OpenAI and Bright Data API Key</h3>
Rename the .env.example file to .env
Add your OpenAI API Key
Add your Bright Data API Key

<h2>Executing the scripts</h2>

- Open a terminal in VS Code

- Execute the following command:

```
python 1_simple_agent.py
python 2_chat_with_agent.py
streamlit run 3_streamlit_chat.py
streamlit run 4_streamlit_chat_with_tools.py
```
