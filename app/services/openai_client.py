from app.core.config import settings
import openai

def run_generation(prompt: str, max_tokens: int = 256):
    if not settings.OPENAI_API_KEY:
        # dummy output
        out = "[DUMMY OUTPUT] Improved proposal suggestion. (Set OPENAI_API_KEY to get real output)\n\n" + prompt[:1000]
        tokens = {"prompt": len(prompt.split()), "completion": 20, "total": len(prompt.split()) + 20}
        return out, tokens

    openai.api_key = settings.OPENAI_API_KEY
    # Use chat completions with messages
    response = openai.ChatCompletion.create(
        model=settings.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are an RFP/Proposal improvement assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=0.2,
    )
    text = response.choices[0].message.content
    usage = getattr(response, 'usage', {})
    tokens = {
        "prompt": getattr(usage, 'prompt_tokens', 0),
        "completion": getattr(usage, 'completion_tokens', 0),
        "total": getattr(usage, 'total_tokens', 0),
    }
    return text, tokens



# def run_generation(prompt: str, max_tokens: int = 256):
#     if not settings.OPENAI_API_KEY:
#         # dummy output
#         out = "[DUMMY OUTPUT] Improved proposal suggestion. (Set OPENAI_API_KEY to get real output)\n\n" + prompt[:1000]
#         tokens = {"prompt": len(prompt.split()), "completion": 20, "total": len(prompt.split()) + 20}
#         return out, tokens

#     openai.api_key = settings.OPENAI_API_KEY
#     # Use chat completions with messages
#     # response = openai.ChatCompletion.create(
#     #     model=settings.OPENAI_MODEL,
#     #     messages=[
#     #         {"role": "system", "content": "You are an RFP/Proposal improvement assistant."},
#     #         {"role": "user", "content": prompt},
#     #     ],
#     #     max_tokens=max_tokens,
#     #     temperature=0.2,
#     # )
#     # text = response.choices[0].message.content
#     usage = getattr({}, 'usage', {})
#     tokens = {
#         "prompt": getattr(usage, 'prompt_tokens', 0),
#         "completion": getattr(usage, 'completion_tokens', 0),
#         "total": getattr(usage, 'total_tokens', 0),
#     }
#     return prompt, tokens
