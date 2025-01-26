# ollama.py
import requests

# عنوان خادم Llama
url = "http://localhost:11434/v1/chat/completions"

def get_response_from_llama(user_input):
    # إعداد البيانات الأولية
    data = {
        "model": "llama3.2:latest",  # اسم النموذج
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        # إرسال الطلب إلى الخادم
        response = requests.post(url, json=data)
        response.raise_for_status()  # التحقق من وجود أي خطأ في الاستجابة
        return response.json()  # إرجاع النتيجة بتنسيق JSON
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"  # معالجة الأخطاء
