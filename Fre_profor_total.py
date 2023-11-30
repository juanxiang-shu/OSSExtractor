import os
import re
import xlwt
from collections import Counter
from Product_form import Product_Form

data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]

total_frequencies = Counter()
for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:
        product_form_instance = Product_Form()
        converted_words = product_form_instance.process_data_file(file_path)

        element_frequencies = Counter(converted_words)
        total_frequencies += element_frequencies

sorted_word2 = sorted(total_frequencies.items(), key=lambda x: x[1], reverse=True)

def process_data_pro(sorted_data):
    result = []
    for word, frequency in sorted_data:
        result.append((word, frequency))
    return result