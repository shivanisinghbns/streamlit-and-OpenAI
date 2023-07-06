# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:14:36 2023

@author: shivani.singh
"""

import streamlit as st
from streamlit_chat import message
from langchain.agents import create_csv_agent
from streamlit_extras.switch_page_button import switch_page
import os
from langchain.llms import OpenAI


os.environ["OPENAI_API_KEY"] = "Your api key"
st.set_page_config(initial_sidebar_state="collapsed",)
st.markdown("<h1 style='text-align: center; color:black;font-family:serif;'>Hey,Let's find out what you need!</h1>", unsafe_allow_html=True)

llm=OpenAI(temperature=0)
agent=create_csv_agent(llm,r"C:\Users\shivani.singh\Test_Code\top_50.csv",verbose=True)
customized_button = st.markdown("""
    <style >
    .stDownloadButton, div.stButton {text-align:center}
    .stDownloadButton button, div.stButton > button:first-child {
        background-color: #ADD8E6;
        color:#000000;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    .stDownloadButton button:hover, div.stButton > button:hover {
        background-color: #ADD8E6;
        color:#000000;
    }
        }
    </style>""", unsafe_allow_html=True)
#hide_pages(['streamlit_chat','streamlit1'])
st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )
placeholder_2 = st.empty()
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

response_container = st.container()

# Opening message from the bot
with response_container:
   r="Hi! How may I help you?"
   emoji_url = "https://api.dicebear.com/5.x/bottts/svg?seed=88"

   st.markdown(
    f'<div style="display: flex; align-items: center;"><img src="{emoji_url}" width="70px" style="margin-right: 10px;">{r}</div>',
    unsafe_allow_html=True
)

# User input
input_container = st.container()
def get_text():
    input_text = st.text_input("You: ", "", key="input",placeholder="Ask your questions here.")
    return input_text

# Response output
with input_container:
    user_input = get_text()

greeting_prompts = { "hello": "Hello! Welcome. How can I assist you today?", 
                    "hi": "Hi there! How can I help you find the perfect product?", 
                    "hey": "Hey! Welcome. How can I assist you?", 
                    "good morning": "Good morning! How may I help you?", 
                    "good afternoon": "Good afternoon! How can I assist you in finding what you need?", 
                    "good evening": "Good evening! How can I help you?", 
                    "greetings": "Greetings! How may I assist you?" }


with response_container:
    if user_input:
        st.session_state['past'].append(user_input)
        if user_input.lower() in greeting_prompts:
            response=greeting_prompts[user_input.lower()]
            print(greeting_prompts[user_input.lower()])
            print("in if block")
            st.session_state['generated'].append(response)

        else:
            response=agent.run(user_input)
            print(response)
        
            st.session_state['generated'].append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            response=st.session_state['generated'][i]

            emoji_url = "https://api.dicebear.com/5.x/bottts/svg?seed=88"

            # Create two columns with appropriate width ratios
            col1, col2 = st.columns([0.1, 0.8])
            
            # Display the emoji image in the first column
            with col1:
                st.image(emoji_url, use_column_width=True)
            
            # Display the message in the second column
            with col2:
                  st.markdown(response)
                  #st.write(len(response))
           
            


if st.button('End Chat'):   
    st.session_state['generated'] = []
    st.session_state['past'] = []
    switch_page('streamlit1')
    
   