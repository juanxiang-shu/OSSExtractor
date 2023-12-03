import re
from element_definitions import reaction_words, element_definitions, temperature_words,\
    compounds_words, compounds1_words, compounds2_words, compounds3_words

def find_words(paragraph):
    reaction_pattern = r"\b(?:{})\b".format("|".join(reaction_words))
    temperature_pattern = r"\b\d+(?:\.\d+)?\s*(?:{})\b".format("|".join(temperature_words))
    temperature_pattern1 = r"\b(RT|rt|room temperature|(RT))\b"
    element_pattern = r"\b(?:{})\b".format("|".join(element_definitions))
    compound_pattern = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words))
    compounds1_pattern = r"\b(?:{})\b".format("|".join(compounds1_words))
    compounds2_pattern = r"\b(?:{})\b".format("|".join(compounds_words))
    compounds3_pattern = r"\b(?:{})\b".format("|".join(compounds2_words))
    compounds4_pattern = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds3_words))

    substrate_pattern = r"({})\((\d+)\)".format(element_pattern)

    matches = re.findall(reaction_pattern, paragraph, re.IGNORECASE)
    reaction = set(matches)

    matches = re.findall(temperature_pattern, paragraph, re.IGNORECASE)
    temperature = {re.sub(r'[\u2009\u2005\u2006\u2007\u2008\u2010\u2011\u2012\u2013]', ' ', temp) for temp in matches}

    matches = re.findall(substrate_pattern, paragraph, re.IGNORECASE)
    substrate = {"{}({})".format(match[0], match[1]) for match in matches}

    matches2 = re.findall(compound_pattern, paragraph, re.IGNORECASE)
    matches = re.findall(compounds1_pattern, paragraph)
    compounds1 = set(matches)
    matches = re.findall(compounds2_pattern, paragraph, re.IGNORECASE)
    compounds2 = set(matches)
    matches = re.findall(compounds3_pattern, paragraph, re.IGNORECASE)
    compounds3 = set(matches)
    matches3 = re.findall(compounds4_pattern, paragraph, re.IGNORECASE)
    all_matches = set(matches3 + matches2)

    def remove_brackets(compound):
        if compound.startswith('[') or compound.startswith('('):
            compound = compound.lstrip('[').lstrip('(')

        if compound.endswith(']') or compound.endswith(')'):
            compound = compound.rstrip(']').rstrip(')')

        return compound

    sorted_matches = sorted(all_matches, key=lambda x: len(remove_brackets(x)), reverse=True)

    complete_compounds = set()
    for match in sorted_matches:
        match_without_brackets = remove_brackets(match)
        if not any(existing_without_brackets[:35] == match_without_brackets[:35] for existing_without_brackets in
                   complete_compounds):
            complete_compounds.add(match_without_brackets)

    def clean_compound(compound):
        cleaned_compound = re.sub(r'[;.,|\d+]+$', '', compound)
        if cleaned_compound.endswith("tion") or cleaned_compound.endswith("ed") or cleaned_compound.endswith("tive")\
                or cleaned_compound.endswith("ing") or cleaned_compound.endswith("1,2,3-triazole")\
                or cleaned_compound.endswith("nic") or cleaned_compound.endswith("-")\
                or cleaned_compound.endswith("type") or cleaned_compound.endswith("alkenes/alkenyl")\
                or cleaned_compound.endswith("alkenes-alkenyl") or cleaned_compound.endswith("aryl–aryl") \
                or cleaned_compound.startswith("iso") or cleaned_compound.endswith("Cl")\
                or cleaned_compound.startswith("Fe/Cu") or cleaned_compound.endswith("azide–alkyne")\
                or cleaned_compound.endswith("poly(arylene") or cleaned_compound.startswith("α")\
                or cleaned_compound.endswith("biphenylene–ethynylene"):
            cleaned_compound = ''
        return cleaned_compound
    compounds_2 = {clean_compound(compound) for compound in compounds1}
    compounds_3 = {clean_compound(compound) for compound in compounds2}
    compounds_4 = {clean_compound(compound) for compound in compounds3}
    compounds_5 = {clean_compound(compound) for compound in complete_compounds}
    compounds_final = {compound for compound in (compounds_5.union(compounds_2)
                                                 - (compounds_3.union(compounds_4))) if compound}

    result = {
        "reaction": reaction,
        "temperature": temperature,
        "substrate": substrate,
        "Compounds": compounds_final
    }
    return result



