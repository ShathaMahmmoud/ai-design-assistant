from validator import validate_brief
from prompts import build_user_prompt
from llm_service import generate_response
from formatter import format_brief


def main():
    user_input = input("اكتب طلب التصميم: ")

    if not validate_brief(user_input):
        print("الطلب فارغ، اكتب تفاصيل التصميم أولًا.")
        return

    prompt = build_user_prompt(user_input)

    brief = generate_response(prompt)

    formatted_brief = format_brief(brief)

    print(formatted_brief)


if __name__ == "__main__":
    main()