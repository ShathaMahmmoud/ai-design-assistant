from validator import validate_brief
from prompts import build_user_prompt
from llm_service import generate_response


user_input = input("اكتب طلب التصميم: ")

if not validate_brief(user_input):
    print("الطلب فارغ، اكتب تفاصيل التصميم أولًا.")

else:
    prompt = build_user_prompt(user_input)
    brief = generate_response(prompt)
    
    print(brief.)