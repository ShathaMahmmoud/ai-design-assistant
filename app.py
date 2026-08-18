import html

import streamlit as st

from validator import validate_brief
from prompts import build_user_prompt
from llm_service import generate_response


st.set_page_config(
    page_title="AI Design Assistant",
    page_icon="🎨",
    layout="centered"
)


# ---------- Styling ----------

st.markdown(
    """
    <style>

    .block-container {
        max-width: 900px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .info-card {
        padding: 20px;
        border: 1px solid rgba(128,128,128,0.20);
        border-radius: 16px;
        margin-bottom: 12px;
        min-height: 105px;
    }

    .card-label {
        color: #888;
        font-size: 13px;
        margin-bottom: 7px;
    }

    .card-value {
        font-size: 20px;
        font-weight: 700;
    }

    .section-title {
        font-size: 18px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 12px;
    }

    .chip {
        display: inline-block;
        padding: 6px 12px;
        margin: 4px;
        border-radius: 999px;
        background: rgba(128,128,128,0.12);
        border: 1px solid rgba(128,128,128,0.15);
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------- Helper Functions ----------

def render_chips(items: list[str]):
    if not items:
        st.caption("غير محدد")
        return

    chips = "".join(
        f'<span class="chip">{html.escape(item)}</span>'
        for item in items
    )

    st.markdown(chips, unsafe_allow_html=True)


def render_list(items: list[str]):
    for item in items:
        st.write(f"• {item}")


# ---------- Header ----------

st.markdown(
    '<div class="main-title">🎨 AI Design Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'حوّل طلب التصميم إلى موجز واضح ومنظم يساعدك تبدأ التصميم بثقة.'
    '</div>',
    unsafe_allow_html=True
)


# ---------- Input ----------

with st.container(border=True):

    user_input = st.text_area(
        "اكتب طلب التصميم",
        placeholder=(
            "مثال: أبي شعار لمقهى اسمه لوز يستهدف الشباب، "
            "بألوان بيج وبني، ويكون بسيط وحديث."
        ),
        height=160
    )

    analyze_button = st.button(
        "تحليل الطلب ✨",
        type="primary",
        use_container_width=True
    )


# ---------- Analysis ----------

if analyze_button:

    if not validate_brief(user_input):
        st.warning("اكتب تفاصيل طلب التصميم أولًا.")

    else:
        prompt = build_user_prompt(user_input)

        try:
            with st.spinner("جاري تحليل طلبك..."):
                brief = generate_response(prompt)

            st.success("تم تحليل الطلب بنجاح")

            st.markdown("## موجز التصميم")

            # ---------- Top Cards ----------

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <div class="card-label">نوع التصميم</div>
                        <div class="card-value">
                            {html.escape(brief.design_type)}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <div class="card-label">اسم البراند</div>
                        <div class="card-value">
                            {html.escape(brief.brand_name)}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <div class="card-label">نوع النشاط</div>
                        <div class="card-value">
                            {html.escape(brief.business_type)}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # ---------- Audience ----------

            with st.container(border=True):
                st.markdown("#### 🎯 الجمهور المستهدف")
                render_chips(brief.target_audience)


            # ---------- Colors & Style ----------

            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=True):
                    st.markdown("#### 🎨 الألوان")
                    render_chips(brief.preferred_colors)

            with col2:
                with st.container(border=True):
                    st.markdown("#### ✨ الأسلوب")
                    render_chips(brief.design_style)


            # ---------- Goal ----------

            with st.container(border=True):
                st.markdown("#### 🎯 هدف التصميم")
                st.write(brief.design_goal)


            # ---------- Required Elements ----------

            if brief.required_elements:
                with st.container(border=True):
                    st.markdown("#### 📌 العناصر المطلوبة")
                    render_list(brief.required_elements)


            # ---------- Missing Information ----------

            if brief.missing_information:
                with st.container(border=True):
                    st.markdown("#### ⚠️ معلومات نحتاجها")
                    render_list(brief.missing_information)


            # ---------- Suggested Directions ----------

            if brief.suggested_directions:
                with st.container(border=True):
                    st.markdown("#### 💡 اتجاهات مقترحة")
                    render_list(brief.suggested_directions)

        except Exception as e:
            st.error("حدث خطأ أثناء تحليل الطلب. حاول مرة أخرى.")

            # نخليه مؤقتًا أثناء التطوير
            st.write(e)