🚀 Moms Verdict AI

A trust-aware, multilingual AI system that transforms unstructured product reviews into structured, decision-ready insights for mothers.

🔗 Demo
🎥 Loom Video: 
💻 Runs locally:
python main.py
🧠 Summary

Moms Verdict AI converts messy, unstructured product reviews into a clear, structured verdict.

Instead of reading dozens of reviews, moms get:

Key pros & cons
Safety signals
Confidence score
Fake review detection
Missing information
Personalized recommendations

All outputs are generated in English and Arabic.

🎯 Problem

Mothers shopping online face:

Too many reviews
Conflicting opinions
Hidden durability/safety issues
Time pressure

👉 This leads to poor or delayed decisions.

⚙️ Solution

This system compresses all reviews into a single structured JSON output that is:

Easy to understand
Reliable
Transparent about uncertainty
📊 Sample Output
{
  "verdict": "Mixed",
  "pros": [
    "Very useful for baby",
    "Good quality"
  ],
  "cons": [
    "A bit expensive",
    "Not very durable",
    "Poor packaging"
  ],
  "safety_flags": [],
  "confidence_score": 0.6,
  "fake_review_ratio": 0.15,
  "missing_info": [
    "long-term durability",
    "safety testing"
  ],
  "best_for": "Babies aged 6-12 months",
  "not_for": "Long-term heavy use",
  "arabic": {
    "verdict": "مختلط",
    "pros": ["مفيد للطفل", "جودة جيدة"],
    "cons": ["غالي", "غير متين", "تغليف سيء"]
  }
}
✨ Key Features
✅ Structured JSON output
✅ Confidence scoring (uncertainty aware)
✅ Fake review detection
✅ Multilingual (English + Arabic)
✅ Missing information detection
✅ Robust to API failures (multi-model fallback + retry)
✅ No hallucination policy
🏗️ Architecture
Reviews
   ↓
Prompt Engineering (few-shot + constraints)
   ↓
Gemini LLM (multi-model fallback)
   ↓
Structured JSON Extraction
   ↓
Validation + Error Handling
   ↓
Final Output (EN + AR)
🔁 Robustness Features
Multi-model fallback (handles API failures)
Retry logic for empty/null outputs
Safe extraction from model responses
Strict JSON enforcement
Graceful handling of missing data
🌍 Multilingual Support

Outputs are generated in:

English (primary)
Arabic (natural, not literal translation)
🧪 Evaluation
Methodology

The system is tested on 10 structured test cases, including:

Positive / negative / mixed reviews
Safety signals
Fake/spam reviews
Missing information
Noisy input
Multilingual input
Edge cases
Metrics
Field extraction accuracy
Verdict correctness
Confidence calibration
Hallucination rate (target: 0%)
JSON validity (100%)
⚖️ Tradeoffs
Design Choices
Structured output > plain summaries
Reliability > creativity
Explicit uncertainty > hidden assumptions
Limitations
Sarcasm detection is limited
Fake review detection is heuristic-based
Depends on input quality
⚙️ Setup
git clone https://github.com/Manipal-kodakandla/moms-verdict-ai.git
cd moms-verdict-ai

pip install -r requirements.txt

set GOOGLE_API_KEY=your_key_here   # Windows
# export GOOGLE_API_KEY=your_key_here (Mac/Linux)

python main.py
🛠️ Tech Stack
Python 3.14
Gemini API (google.genai)
Prompt Engineering
JSON validation
🤖 AI Usage
Prompt design and refinement
Structured output generation
Debugging and failure handling
Evaluation design
🚧 Future Improvements
Real-time integration with product pages
Review clustering (topics: safety, durability, price)
Personalization (child age, preferences)
UI dashboard
⏱️ Time Spent
Problem design: 45 min
Implementation: 2.5 hrs
Debugging & API handling: 1 hr
Evaluation + documentation: 1 hr
🎥 Demo

👉 (Add your Loom link here)

📌 Final Note

This system is not just a review summarizer — it is designed to reason about trust, uncertainty, and decision-making, which are critical for mothers making purchase decisions.
