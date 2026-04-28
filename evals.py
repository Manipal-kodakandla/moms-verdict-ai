import json
from main import analyze_reviews


def run_test(test_name, reviews, checks):
    print(f"\n🧪 Running: {test_name}")

    try:
        result = analyze_reviews(reviews)

        if isinstance(result, str):
            data = json.loads(result)
        else:
            data = result

        passed = True

        for check_name, condition in checks.items():
            if not condition(data):
                print(f"❌ Failed: {check_name}")
                passed = False
            else:
                print(f"✅ Passed: {check_name}")

        if passed:
            print("🎉 Test Passed")
        else:
            print("⚠️ Test Failed")

    except Exception as e:
        print("❌ Error:", e)



tests = [

    {
        "name": "All Positive Reviews",
        "reviews": "Great product, very useful, excellent quality",
        "checks": {
            "pros >= 2": lambda d: len(d["pros"]) >= 2,
            "cons empty": lambda d: len(d["cons"]) == 0,
            "verdict recommended": lambda d: d["verdict"] == "Recommended",
            "confidence > 0.7": lambda d: d["confidence_score"] > 0.7,
        }
    },

    {
        "name": "All Negative Reviews",
        "reviews": "Very bad quality, broke quickly, waste of money",
        "checks": {
            "cons >= 2": lambda d: len(d["cons"]) >= 2,
            "pros empty": lambda d: len(d["pros"]) == 0,
            "verdict not recommended": lambda d: d["verdict"] == "Not Recommended",
        }
    },

    {
        "name": "Mixed Reviews",
        "reviews": "Good quality but expensive and not durable",
        "checks": {
            "pros >= 1": lambda d: len(d["pros"]) >= 1,
            "cons >= 1": lambda d: len(d["cons"]) >= 1,
            "verdict mixed": lambda d: d["verdict"] == "Mixed",
        }
    },

    {
        "name": "Safety Detection",
        "reviews": "Product caused rash on baby skin",
        "checks": {
            "safety flag present": lambda d: len(d["safety_flags"]) > 0,
            "not recommended": lambda d: d["verdict"] != "Recommended",
        }
    },

    {
        "name": "Fake Review Detection",
        "reviews": "Best product ever!!! Amazing!!! Must buy!!!",
        "checks": {
            "fake ratio > 0.3": lambda d: d["fake_review_ratio"] > 0.3,
        }
    },

    {
        "name": "Missing Info",
        "reviews": "Nice product",
        "checks": {
            "missing info exists": lambda d: len(d["missing_info"]) > 0,
            "confidence < 0.5": lambda d: d["confidence_score"] < 0.5,
        }
    },

    {
        "name": "Conflicting Reviews",
        "reviews": "Great quality but broke after 2 days",
        "checks": {
            "pros and cons": lambda d: len(d["pros"]) > 0 and len(d["cons"]) > 0,
            "verdict mixed": lambda d: d["verdict"] == "Mixed",
        }
    },

    {
        "name": "Noisy Input",
        "reviews": "asdf good product 123 ??? bad packaging !!!",
        "checks": {
            "extract pros": lambda d: len(d["pros"]) > 0,
            "extract cons": lambda d: len(d["cons"]) > 0,
        }
    },

    {
        "name": "Multilingual Input",
        "reviews": "Good product, جيد جدا لكن غالي",
        "checks": {
            "pros extracted": lambda d: len(d["pros"]) > 0,
            "cons extracted": lambda d: len(d["cons"]) > 0,
        }
    },

    {
        "name": "Empty Input",
        "reviews": "",
        "checks": {
            "confidence 0": lambda d: d["confidence_score"] == 0,
        }
    },

]


if __name__ == "__main__":
    for test in tests:
        run_test(test["name"], test["reviews"], test["checks"])
