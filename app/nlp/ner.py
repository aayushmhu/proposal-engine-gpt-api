try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except Exception:
    nlp = None

def extract_entities(text: str):
    if not nlp:
        return {}
    doc = nlp(text)
    ents = {}
    for ent in doc.ents:
        ents.setdefault(ent.label_, []).append(ent.text)
    return ents
