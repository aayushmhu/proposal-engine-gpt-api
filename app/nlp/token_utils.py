try:
    import tiktoken
except Exception:
    tiktoken = None

def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    if not text:
        return 0
    if tiktoken:
        try:
            enc = tiktoken.encoding_for_model(model)
        except Exception:
            enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    # fallback rough count by words
    return len(text.split())
