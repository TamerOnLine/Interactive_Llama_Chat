# streamlit.py
import streamlit as st
from ollama import get_response_from_llama  # استيراد الدالة من ollama.py

def streamlit_app():
    # عنوان الصفحة
    st.title("Chat with Llama")

    # نص التفاعل مع المستخدم
    user_input = st.text_input("Enter your message:")

    if user_input:
        # الحصول على الرد من الخادم
        response = get_response_from_llama(user_input)
        
        # عرض الاستجابة
        #st.write("Response from Llama:", response)

        # استخراج الرد النصي من الاستجابة JSON
        if isinstance(response, dict) and 'choices' in response:
            content = response['choices'][0]['message']['content']
            st.write("Response from Llama:", content)  # عرض النص فقط من الرد
        else:
            st.write("Error in response:", response)  # إذا كانت الاستجابة غير صحيحة
