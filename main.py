import os
import json
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

PROMPT = """
You are an AI system that extracts structured insights from product reviews for mothers shopping on an e-commerce platform.

Your goal is to produce a reliable, decision-ready summary.

STRICT REQUIREMENTS:
- Output ONLY valid JSON (no explanation, no markdown)
- Always extract insights if ANY signal exists
- Do NOT hallucinate facts not present in reviews
- If information is missing, include it in "missing_info"

OUTPUT FORMAT:
{
  "verdict": "Recommended" | "Not Recommended" | "Mixed",
  "pros": [list of concise phrases],
  "cons": [list of concise phrases],
  "safety_flags": [list],
  "confidence_score": float,
  "fake_review_ratio": float,
  "missing_info": [list],
  "best_for": string,
  "not_for": string,
  "arabic": {
    "verdict": string,
    "pros": [list],
    "cons": [list],
    "safety_flags": [list],
    "confidence_score": float,
    "fake_review_ratio": float,
    "missing_info": [list],
    "best_for": string,
    "not_for": string
  }
}

GUIDELINES:
- Extract short phrases (not sentences)
- Confidence:
  - High (0.7–0.9): strong agreement
  - Medium (0.4–0.7): mixed
  - Low (<0.4): weak signal
- Detect exaggerated reviews for fake_review_ratio

Analyze the following reviews:
"""

def call_model(prompt):
    try:
        return client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
    except Exception:
        print("⚠️ Switching to fallback model...")
        return client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

def extract_text(response):
    try:
        if response.text:
            return response.text
        return response.candidates[0].content.parts[0].text
    except:
        return None

def analyze_reviews(reviews):
    prompt = PROMPT + "\n\n" + reviews

    response = call_model(prompt)
    output = extract_text(response)

    if not output or output == "null":
        print("⚠️ Empty response, retrying...")
        response = call_model(prompt)
        output = extract_text(response)

    if not output:
        print("❌ Model failed to generate output")
        return

    output = output.replace("```json", "").replace("```", "").strip()

    print("\nRAW OUTPUT:\n", output)

    try:
        data = json.loads(output)
        print("\nVALID JSON OUTPUT:\n", json.dumps(data, indent=2))
    except Exception as e:
        print("\n❌ JSON ERROR:", e)


if __name__ == "__main__":
    with open("data/sample_reviews.txt", "r", encoding="utf-8") as f:
        reviews = f.read()

    analyze_reviews(reviews)
