from schemas import DesignBrief


def format_list(items: list[str]) -> str:
    return "\n".join(f"• {item}" for item in items)


def format_section(title: str, items: list[str]) -> str:
    if not items:
        return ""

    return f"""
{title}
{format_list(items)}
"""


def format_brief(brief: DesignBrief) -> str:
    output = f"""
📋 موجز التصميم

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎨 نوع التصميم:
{brief.design_type}

🏢 اسم البراند:
{brief.brand_name}

☕ نوع النشاط:
{brief.business_type}

🎯 الجمهور المستهدف:
{format_list(brief.target_audience)}

🎯 هدف التصميم:
{brief.design_goal}

🎨 الألوان المفضلة:
{format_list(brief.preferred_colors)}

✨ أسلوب التصميم:
{format_list(brief.design_style)}
"""

    output += format_section(
        "📌 العناصر المطلوبة:",
        brief.required_elements
    )

    output += format_section(
        "❓ المعلومات الناقصة:",
        brief.missing_information
    )

    output += format_section(
        "💡 الاتجاهات المقترحة:",
        brief.suggested_directions
    )

    return output