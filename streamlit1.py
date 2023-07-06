import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages
st.set_page_config(initial_sidebar_state="collapsed",)
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
left_co, cent_co,last_co = st.columns(3)
col1, col2, col3 = st.columns([1,8,1])
st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )
hide_pages(['streamlit_chat','streamlit1'])
with col1:
    st.write("")

with cent_co:
    p=st.image(
            #"gif.gif", # I prefer to load the GIFs using GIPHY
            "gif.gif",
            
        # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )
with col2:
    

    if st.button('Start New Chat!(CSV)'):
         switch_page('streamlit_csv')
   
with col3:
    st.write("")






    