from app.nlp.postprocess import sectionize

def split_into_sections(text: str):
    return sectionize(text)
