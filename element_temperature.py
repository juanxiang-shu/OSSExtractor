import os
import re
from itertools import combinations
import matplotlib.pyplot as plt
from Compounds import find_words
from Reactions import reaction
from element_definitions import element_definitions
from Precursors import extract_precursors
from Product import extract_products
from Fre_Tem_total import convert_to_K
from element_definitions import temperature_words

data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]
element_results = []
temperature_results = []
all_transactions = []
for file_path in data_files:
    with open(file_path, "r", encoding="utf-8") as file:
        paragraph = file.read()
        pattern = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
        cleaned_paragraph = re.sub(pattern, '', paragraph)
        paragraph = cleaned_paragraph

        result_ele = find_words(paragraph)
        element = result_ele["element"]
        element_results.append(element)

        temperature_pattern = r"\b\d+(?:\.\d+)?\s*(?:{})\b".format("|".join(temperature_words))
        paragraph = re.sub(temperature_pattern, convert_to_K, paragraph)
        result_tem = find_words(paragraph)
        temperature_set = result_tem["temperature"]
        temperature = {temp.replace(" ", "") for temp in temperature_set}
        temperature_results.append(temperature)

        result_sub = find_words(paragraph)
        substrate = result_sub["substrate"]

        result_rea = reaction(paragraph)
        reactions = result_rea

        result_pre = extract_precursors(paragraph)
        precursors = result_pre

        result_pro = extract_products(paragraph)
        products = result_pro

        combined_set = set(element) | set(temperature)
        all_transactions.append(list(combined_set))

def generate_candidates(itemset, length):
    candidates = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            candidate = itemset[i] | itemset[j]
            if len(candidate) == length:
                candidates.append(candidate)
    return candidates

def prune(itemset, candidates):
    pruned_candidates = []
    for candidate in candidates:
        is_valid = True
        subsets = [candidate - {item} for item in candidate]
        for subset in subsets:
            if subset not in itemset:
                is_valid = False
                break
        if is_valid:
            pruned_candidates.append(candidate)
    return pruned_candidates

def apriori(dataset, min_support):
    itemset = [frozenset([item]) for transaction in dataset for item in transaction]
    frequent_itemsets = []

    k = 2
    while itemset:
        candidates = generate_candidates(itemset, k)
        counts = {candidate: 0 for candidate in candidates}

        for transaction in dataset:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    counts[candidate] += 1

        frequent_itemset = [candidate for candidate, count in counts.items() if count >= min_support]
        frequent_itemsets.extend(frequent_itemset)

        itemset = prune(frequent_itemset, candidates)
        k += 1

    return frequent_itemsets

def apriori_analysis(dataset, min_support):
    frequent_itemsets = apriori(dataset, min_support)
    return frequent_itemsets


def calculate_confidence(rule, frequent_itemsets):
    antecedent, consequent = rule
    support_antecedent = get_support(antecedent, frequent_itemsets)
    support_rule = get_support(set(antecedent) | set(consequent), frequent_itemsets)
    confidence = support_rule / support_antecedent
    return confidence

def get_support(itemset, all_transactions):
    count = 0
    for transaction in all_transactions:
        if itemset.issubset(transaction):
            count += 1
    return count / len(all_transactions)


def generate_association_rules(frequent_itemsets, min_confidence):
    association_rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            subsets = list(combinations(itemset, len(itemset) - 1))  # Generate all possible subsets of size len(itemset) - 1
            for antecedent in subsets:
                antecedent_set = set(antecedent)
                consequent = itemset - antecedent_set
                confidence = calculate_confidence((antecedent_set, consequent), frequent_itemsets)
                if confidence >= min_confidence:
                    association_rules.append((antecedent_set, consequent, confidence))
    return association_rules

min_support = 70
min_confidence = 0.6
frequent_itemsets = apriori_analysis(all_transactions, min_support)

itemset_elements = []
for itemset in frequent_itemsets:
    ele = list(itemset)
    itemset_elements.append(ele)

def filter_element_items(itemset_list):
    filtered_itemset_list = []
    for itemset in itemset_list:
        if all(element in element_definitions for element in itemset):
            continue
        if all(element.endswith('K') for element in itemset):
            continue
        else:
            filtered_itemset_list.append(itemset)
    return filtered_itemset_list

filtered_itemset_elements = filter_element_items(itemset_elements)
data = filtered_itemset_elements

element_temperature_data = {'elements': [], 'temperatures': []}
for itemset in data:
    for item in itemset:
        if 'K' in item:
            element_temperature_data['temperatures'].append(float(item.replace('K', '')))
        else:
            element_temperature_data['elements'].append(item)

plt.figure(figsize=(10, 6))
plt.bar(element_temperature_data['elements'], element_temperature_data['temperatures'])
plt.xlabel("Element")
plt.ylabel("Temperature (K)")
plt.title("Element vs Temperature")
plt.show()
