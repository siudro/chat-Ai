import streamlit as st
import openai

st.title("تكلم مع اينشتاين🧠")

"""
مرحبا أنا اينشتاين 
امرني وش بغيت؟🧠
"""

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "انت اسمك اينشتاين, انت اذكى رجل في العالم, وتحب استخدام الايموجي,وتستطيع الاجابة على جميع الاسئله , وانت شخص محترم,وتعرف ترد على الناس بأدب"}
    ]

user_input = st.text_input("أسألني شيء:", key="user_input")

if user_input:
    openai.api_key = st.secrets["api"]
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=st.session_state.messages)
    ai_response = response.choices[0].message
    st.session_state.messages.append(ai_response)
    st.chat_message("assistant").write(ai_response.content)