import streamlit as st

from validator import validate_brief
from prompts import build_user_prompt
from llm_service import generate_response
from formatter import format_brief


st.set_page_config(
    page_title="AI Design Assistant",
    page_icon="🎨",
    layout="centered"
)


st.title("AI Design Assistant 🎨")

st.write(
    "حوّل طلب التصميم إلى موجز واضح ومنظم للمصمم."
)


user_input = st.text_area(
    "اكتب طلب التصميم",
    placeholder="مثال: أبي شعار لمقهى اسمه لوز يستهدف الشباب، بألوان بيج وبني، ويكون بسيط وحديث.",
    height=150
)


if st.button("تحليل الطلب"):

    if not validate_brief(user_input):
        st.warning("اكتب تفاصيل طلب التصميم أولًا.")

    else:
        prompt = build_user_prompt(user_input)

        try:
            with st.spinner("جاري تحليل طلبك..."):
                brief = generate_response(prompt)

            formatted_brief = format_brief(brief)

            st.success("تم تحليل الطلب بنجاح")
            st.text(formatted_brief)

        except Exception as e:
            st.error("حدث خطأ أثناء تحليل الطلب. حاول مرة أخرى.")

            # مؤقتًا أثناء التطوير حتى نعرف سبب أي خطأ
            st.write(e)