import re
from abc import ABC, abstractmethod # Abstract Base Class

class BaseChunkSplitter(ABC):
    @abstractmethod
    def split(self, text:str) -> list[str]:
        pass

class WordCountSplitter(BaseChunkSplitter):
    def __init__(self, max_words: int = 15):
        self.max_words = max_words

    def split(self, text: str) -> list[str]:
        text = text.replace("\n", " ")
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []

        for sentence in sentences:
            words = sentence.split()

            if len(words) <= self.max_words:
                if sentence.strip():
                    chunks.append(sentence.strip())
            else:
                for i in range(0, len(words), self.max_words):
                    chunk = " ".join(words[i:i + self.max_words])
                    chunks.append(chunk.strip())

        return chunks

# Add other splitter after lv2
# class PunctuationSplitter(BaseChunkSplitter):
# class SpacyDependencySplitter(BaseChunkSplitter):

def split_text(text: str, max_words: int = 15) -> list[str]:
    splitter = WordCountSplitter(max_words=max_words)
    return splitter.split(text)
