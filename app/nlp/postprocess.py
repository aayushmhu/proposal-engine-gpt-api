def sectionize(text: str, desired_sections=None):
    # Very simple splitter: find common section headings; fallback entire text as 'body'
    if not desired_sections:
        desired_sections = ["Introduction","Scope","Deliverables","Timeline","Assumptions"]

    sections = {}
    lower = text.lower()
    for s in desired_sections:
        idx = lower.find(s.lower())
        if idx != -1:
            # crude: split at heading occurrence
            sections[s] = text[idx: idx + 1000]  # truncated grab
    if not sections:
        sections["Body"] = text
    return sections
