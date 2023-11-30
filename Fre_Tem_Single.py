import os
import re
from collections import Counter
from Compounds import find_words

data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]

for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:

        paragraph = file.read()
        pattern = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
        cleaned_paragraph = re.sub(pattern, '', paragraph)
        paragraph = cleaned_paragraph
        result = find_words(paragraph)
        substrate_frequencies = Counter(result["temperature"])
        sorted_words = sorted(substrate_frequencies.items(), key=lambda x: x[1], reverse=True)
        print("Temperature Frequencies:")
        for word, frequency in sorted_words:
            print(f"{word}: {frequency}")