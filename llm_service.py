from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT
from schemas import DesignBrief

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str) -> DesignBrief:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema=DesignBrief,
        ),
    )

    return response.parsed