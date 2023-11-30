import re
from collections import Counter
from Compounds import find_words

def clean_compound(compound):
    cleaned_compound = re.sub(r'[;.,|\d+]+$', '', compound)
    if cleaned_compound.endswith("tion") or cleaned_compound.endswith("ed"):
        cleaned_compound = ''
    return cleaned_compound

def count_word_occurrences(paragraph, compounds_final):
    word_counts = Counter(paragraph.split())
    word_occurrences = {word: word_counts[word] for word in compounds_final}
    most_common_word = max(word_occurrences, key=word_occurrences.get)
    return most_common_word

def extract_products(paragraph):
    products = set()
    sentences = paragraph.split(".")
    After_pattern = r'\b(In summary|In conclusion|To conclude)\b'
    demonstrate_pattern = r'\b(we demonstrate|we have demonstrated|on-surface synthesis of|Figure 2 c)\b'

    for sentence in sentences:
        sentence = sentence.strip()
        if re.search(After_pattern, sentence, re.IGNORECASE):
            result = find_words(sentence)
            products |= set(result["Compounds"])
        if re.search(demonstrate_pattern, sentence, re.IGNORECASE):
            result = find_words(sentence)
            products |= set(result["Compounds"])

    return products