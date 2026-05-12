from collections import Counter
import re

def count_words(text: str) -> dict:
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words).most_common(5))

if __name__ == "__main__":
    sample = "Git это система контроля версий. Git помогает командам работать вместе."
    print("Топ-5 слов:", count_words(sample))
