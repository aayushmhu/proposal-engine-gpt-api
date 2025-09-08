import re
from collections import Counter

def extract_keywords(text: str, top_n=10):
    words = re.findall(r"\w+", text.lower())
    stop = set(["the","and","of","in","to","for","a","an","is","that"])
    words = [w for w in words if w not in stop and len(w) > 2]
    most = Counter(words).most_common(top_n)
    return [w for w,_ in most]
