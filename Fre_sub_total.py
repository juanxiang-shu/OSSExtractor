import os
import re
import xlwt
from collections import Counter
from Temperature_Substrate import extract_substrate

data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]

total_frequencies = Counter()

for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:
        paragraph = file.read()

        pattern = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
        cleaned_paragraph = re.sub(pattern, '', paragraph)
        paragraph = cleaned_paragraph

        result = extract_substrate(paragraph)
        substrate_frequencies = Counter(result)

        total_frequencies += substrate_frequencies

sorted_words = sorted(total_frequencies.items(), key=lambda x: x[1], reverse=True)

def process_data_sub(sorted_data):
    result = []
    for word, frequency in sorted_data:
        result.append((word, frequency))
    return result
