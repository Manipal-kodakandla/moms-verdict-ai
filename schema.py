from pydantic import BaseModel
from typing import List

class Verdict(BaseModel):
    verdict: str
    pros: List[str]
    cons: List[str]
    safety_flags: List[str]
    confidence_score: float
    fake_review_ratio: float
    missing_info: List[str]
    best_for: str
    not_for: str