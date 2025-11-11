import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if api_key and api_key.startswith("="):
    api_key = api_key.lstrip("=")
client = OpenAI(api_key=api_key)

def analyze_text_with_ai(text: str):
    """
    Performs compliance, grammar scoring, and sentiment analysis using GPT.
    """
    prompt = f"""
    You are an AI compliance and linguistic analysis expert.
    Analyze the following text for:
    - Grammar correctness (0–100 score)
    - Tone and sentiment (positive, neutral, negative)
    - Clarity and professionalism
    - Structural and formatting recommendations

    Return your output strictly in JSON format:
    {{
      "summary": "<Brief overview of document>",
      "grammar_score": <number between 0 and 100>,
      "sentiment": "<positive | neutral | negative>",
      "recommendations": ["list of recommendations"],
      "compliance_score": "<percentage>"
    }}

    Text to analyze:
    {text[:5000]}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in grammar scoring, tone analysis, and compliance evaluation."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    try:
        clean_json = result.strip().replace("```json", "").replace("```", "")
        return json.loads(clean_json)
    except Exception:
        return {
            "summary": "Parsing error",
            "grammar_score": 0,
            "sentiment": "unknown",
            "recommendations": [],
            "compliance_score": "N/A"
        }
