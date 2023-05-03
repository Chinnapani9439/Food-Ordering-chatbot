import streamlit as st
import streamlit.components.v1 as components
import extra_streamlit_components as stx

st.set_page_config(layout="wide")
# import streamlit_theme as stt
padding = 0
#st.markdown(f""" <style>
#    .reportview-container .main .block-container{{
#        padding-top: {padding}rem;
#        padding-right: {padding}rem;
#        padding-left: {padding}rem;
#        padding-bottom: {padding}rem;
#    }} </style> """, unsafe_allow_html=True)
#stt.set_theme({'primary': '#1b3388'})

val = stx.stepper_bar(steps=["Welcome to Wendy's", "Choose Your Delicacy", "Place the Order"])
col1, col2 =  st.beta_columns([2.5, 1])
with col1:    
    #st.image('logo.jpeg', width = 200)
    #st.info(f'{val}')
    flag1=False
    flag2=False
    if val==1:
        flag1=True
    elif val==2:
        flag2=True
    elif val==0:
        st.image('wendys_3.jpg')
    my_expander = st.beta_expander(label='Menu', expanded=flag1)
    with my_expander:
        components.iframe("https://order.wendys.com/categories?site=menu", height=500, scrolling=True)
    my_expander = st.beta_expander(label='Order',expanded=flag2)
    with my_expander:
        components.iframe("https://order.wendys.com/location", height=500, scrolling=True)
    

with col2:
    components.html("""
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  intent="WELCOME"
  chat-title="Wendys_Chat_Bot"
  agent-id="4e2882a6-9078-4cff-a81f-6e7c935f7387"
  language-code="en"
></df-messenger>
""",
    height=550, scrolling=False
)

