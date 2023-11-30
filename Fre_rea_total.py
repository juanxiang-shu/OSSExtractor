import os
import re
from collections import Counter
from Reactions import reaction
from Reactions import get_categories

data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]

total_frequencies = Counter()

for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:
        paragraph = file.read()

        pattern = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
        cleaned_paragraph = re.sub(pattern, '', paragraph)
        paragraph = cleaned_paragraph

        result = reaction(paragraph)
        reactions_frequencies = Counter(result)

        resultcate = get_categories(paragraph)
        reactionscate_frequencies = Counter(resultcate)

        total_frequencies += reactions_frequencies

sorted_word1 = sorted(total_frequencies.items(), key=lambda x: x[1], reverse=True)
sorted_word2 = [item[0] for item in sorted(total_frequencies.items(), key=lambda x: x[1], reverse=True)]

def process_data_rea(sorted_word):
    result = []
    for word, frequency in sorted_word:
        result.append((word, frequency))
    return result

def rea(sorted_word):
    result = []
    for word in sorted_word:
        result.append(word)
    return result