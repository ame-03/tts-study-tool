import re

def split_text(text: str, max_words=15):
    text = text.replace("\n", " ")

    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []

    for sentence in sentences:
        words = sentence.split()

        if len(words) <= max_words:
            if sentence.strip():
                chunks.append(sentence.strip())
        else:
            for i in range(0, len(words), max_words):
                chunk = " ".join(words[i:i+max_words])
                chunks.append(chunk.strip())

    return chunks            