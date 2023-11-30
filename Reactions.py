import re
from collections import Counter
from element_definitions import reaction_words
from collections import defaultdict

def reaction(paragraph):
    reactions = set()
    sentences = paragraph.split(".")
    Before_pattern = r'\b(In this work|Here|Herein|In this communication|In our study|In this article|(Scheme 1))\b'
    After_pattern = r'\b(In summary|In conclusion|To conclude|Conclusions|In conclusion,|To conclude,|SCOF-1)\b'

    for i in range(len(sentences)):
        sentence = sentences[i].strip()
        if re.search(Before_pattern, sentence, re.IGNORECASE):
            context = " ".join(sentences[i:i + 5])
            reaction_pattern = "|".join([r"\b{}\b".format(reaction) for category in reaction_words.values() for reaction in category.keys()])
            reactions |= set(re.findall(reaction_pattern, context, re.IGNORECASE))

        if re.search(After_pattern, sentence, re.IGNORECASE):
            context_1 = " ".join(sentences[i:i + 5])
            reaction_pattern_1 = "|".join([r"\b{}\b".format(reaction) for category in reaction_words.values() for reaction in category.keys()])
            reactions |= set(re.findall(reaction_pattern_1, context_1, re.IGNORECASE))

    reaction_counts = Counter(reactions)

    if reaction_counts:
        max_count = max(reaction_counts.values())
        most_common_reactions = [reaction for reaction, count in reaction_counts.items() if count == max_count]

        matched_subcategories = set()
        for react in most_common_reactions:
            for category, subcategories in reaction_words.items():
                for subcategory, subcategory_keywords in subcategories.items():
                    if any(keyword.lower() in react.lower() for keyword in subcategory_keywords):
                        matched_subcategories.add(subcategory)

        return matched_subcategories
    else:
        reaction_final_pattern = "|".join(
            [r"\b{}\b".format(reaction) for category in reaction_words.values() for subcategories in category.values()
             for reaction in subcategories])
        reaction_final_matches = re.findall(reaction_final_pattern, paragraph, re.IGNORECASE)

        if len(reaction_final_matches) > 1:
            reaction_final_counts = Counter(word for word in reaction_final_matches if word in paragraph)
            max_count_final = max(reaction_final_counts.values())
            most_common_final_reactions = [reaction for reaction, count in reaction_final_counts.items() if
                                           count == max_count_final]

            matched_subcategories = set()
            for react in most_common_final_reactions:
                for category, subcategories in reaction_words.items():
                    for subcategory, subcategory_keywords in subcategories.items():
                        if any(keyword.lower() in react.lower() for keyword in subcategory_keywords):
                            matched_subcategories.add(subcategory)

            return matched_subcategories

        else:
            return set()

def get_categories_from_subcategories(subcategories):
    categories = set()
    for subcategory in subcategories:
        for category, subcats in reaction_words.items():
            if subcategory in subcats:
                categories.add(category)
    return categories

def get_categories(paragraph):
    subcategories = reaction(paragraph)
    if not subcategories:
        return set()
    return get_categories_from_subcategories(subcategories)
