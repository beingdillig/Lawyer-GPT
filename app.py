from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an Indian law expert AI. Answer only questions related to Indian laws and penal codes. Provide precise and structured explanations based on the IPC (Indian Penal Code) sections, Do not answer strictly anything beyond law, legal, IPC."),
    ("human", "Question: {text}"),
])


# UI
st.title("LAWyer GPT")
input_text = st.text_area("Ask Anything.....")
submit = st.button("Ask")

# Load Model (phi4-mini)
llm = Ollama(model="mistral")
output_parser = StrOutputParser() #Converts the model's output to human readable text

if submit and input_text:
    chain = prompt | llm | output_parser
    # formatted_prompt = prompt.format_messages(text=input_text)[1].content  # Only the user message

    with st.spinner("Thinking..."):
        response = ""
        # Placeholder to update text in place
        output_box = st.empty()

        for chunk in chain.stream({"text":input_text}):
            response += chunk
            output_box.markdown(response)  # updates in place
