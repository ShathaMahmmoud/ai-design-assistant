from pydantic import BaseModel


class DesignBrief(BaseModel):
    is_sufficient: bool
    design_type: str
    brand_name: str
    business_type: str
    target_audience: list[str]
    design_goal: str
    preferred_colors: list[str]
    design_style: list[str]
    required_elements: list[str]
    missing_information: list[str]
    suggested_directions: list[str]