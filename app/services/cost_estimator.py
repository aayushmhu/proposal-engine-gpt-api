# Simple rate table (per 1k tokens)
RATES = {
    "gpt-3.5-turbo": 0.002,  # example
    "gpt-4o-mini": 0.03,
}

def estimate_cost(prompt_tokens: int, completion_tokens: int, model: str):
    rate = RATES.get(model, 0.002)
    total_k = (prompt_tokens + completion_tokens) / 1000.0
    return round(total_k * rate, 6)
