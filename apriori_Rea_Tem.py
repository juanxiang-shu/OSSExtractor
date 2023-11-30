import os
import re
import seaborn as sns
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt
from Reactions import get_categories
from Temperature_Substrate import extract_temperature
from Fre_Tem_total import convert_to_K
from element_definitions import reaction_words
from matplotlib.colors import LinearSegmentedColormap

class AprioriReaTem:
    def __init__(self):
        data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]
        all_transactions = []
        for file_path in data_files:
            with open(file_path, "r", encoding="utf-8") as file:
                paragraph = file.read()
                pattern = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
                cleaned_paragraph = re.sub(pattern, '', paragraph)
                paragraph = cleaned_paragraph

                temperature_pattern = r"\b\d+\.\d+\s*(?:°C|K)\b"
                paragraph = re.sub(temperature_pattern, convert_to_K, paragraph)
                result_tem = extract_temperature(paragraph)
                temperature = {temp.replace(" ", "") for temp in result_tem}
                converted_sorted_words = []
                for temp in temperature:
                    if '°C' in temp:
                        temperature_value = float(temp.replace('°C', '')) + 273.15
                        converted_temperature = f"{temperature_value} K"
                        converted_sorted_words.append(converted_temperature)
                    else:
                        converted_sorted_words.append(temp)

                result_rea = get_categories(paragraph)
                reactions = result_rea

                combined_set = set(reactions) | set(converted_sorted_words)
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

        def generate_association_rules(frequent_itemsets):
            matrix = []
            # association_rules = []
            for itemset in frequent_itemsets:
                if len(itemset) > 1:
                    subsets = list(combinations(itemset, len(itemset) - 1))
                    for antecedent in subsets:
                        antecedent_set = set(antecedent)
                        consequent = itemset - antecedent_set
                        confidence = calculate_confidence((antecedent_set, consequent), frequent_itemsets)
                        matrix.append((antecedent_set, consequent, confidence))
            return matrix

        min_support = 80
        frequent_itemsets = apriori_analysis(all_transactions, min_support)
        self.matrix = generate_association_rules(frequent_itemsets)

    def generate_heatmap1(self):
        matrix_1 = []
        for antecedent, consequent, confidence in self.matrix:
            antecedent_str = ', '.join(antecedent)
            consequent_str = ', '.join(consequent)
            matrix_1.append((antecedent_str, consequent_str, confidence))

        itemset_elements = []
        for itemset in matrix_1:
            ele = list(itemset)
            if ele[0] in reaction_words and ele[1] in reaction_words:
                continue
            if ele[0].endswith('K') and ele[1].endswith('K'):
                continue
            else:
                itemset_elements.append(ele)

        itemset_elements1 = []
        for itemset2 in itemset_elements:
            ele = list(itemset2)
            if ele[0] in reaction_words and ele[1].endswith('K'):
                continue
            else:
                itemset_elements1.append(ele)

        association_confidences = {}

        # itemset_elements1
        for antecedent, consequent, confidence in itemset_elements1:
            association_confidences[(frozenset(antecedent), consequent)] = confidence

        # 创建热图数据矩阵
        unique_antecedents = set()
        unique_consequents = set()

        for antecedent, consequent, confidence in itemset_elements1:
            unique_antecedents.add(antecedent)
            unique_consequents.add(consequent)

        antecedents = sorted(list(unique_antecedents), key=lambda x: str(x))
        consequents = sorted(list(unique_consequents), key=lambda x: str(x))
        data_for_heatmap = np.zeros((len(antecedents), len(consequents)))

        for i, antecedent in enumerate(antecedents):
            for j, consequent in enumerate(consequents):
                antecedent_set = frozenset(antecedent)
                confidence = association_confidences.get((antecedent_set, consequent), 0)
                data_for_heatmap[i, j] = confidence

        plt.ion()
        if data_for_heatmap.size == 0:
            plt.figure(figsize=(12, 12))
            plt.text(0.5, 0.5, "No valid data associations under set conditions!",
                     fontsize=14, ha='center', va='center')
            plt.axis('off')  # 隐藏坐标轴
        else:
            # custom_cmap = LinearSegmentedColormap.from_list("custom",
            #                                                 ['#A6D5DB', '#EAA9C1', '#FACABC', '#CCDCAD', '#F3A17C',
            #                                                  '#DBA6D5', '#A6DBC6'])
            custom_cmap = LinearSegmentedColormap.from_list("custom",
                                                            ['#E8F4F5', '#D3EAED', '#A6D5DB',
                                                             '#A6DBC6', '#7C9FA4'])
            sns.set()
            plt.figure(figsize=(12, 12))
            ax = sns.heatmap(data_for_heatmap, cmap=custom_cmap, xticklabels=[str(c) for c in consequents],
                             yticklabels=antecedents, linewidths=1, cbar=True, cbar_kws={"pad": 0.15,
                                                                                         # 'orientation': 'horizontal',
                                                                                         },
            # sns.set()
            # plt.figure(figsize=(12, 12))
            # ax = sns.heatmap(data_for_heatmap, cmap='bwr', xticklabels=[str(c) for c in consequents],
            #                  yticklabels=antecedents, linewidths=1, cbar=True, cbar_kws={"pad": 0.15,
            #                                                                                # 'orientation': 'horizontal',
            #                                                                                },
                             # annot_kws={"size": 20}
                             )
            ax.set_xlabel("Consequent", fontsize=34)
            ax.set_ylabel("Antecedent", fontsize=34)
            ax.tick_params(axis='x', labelsize=30)
            ax.tick_params(axis='y', labelsize=30)
            plt.xticks(rotation=0)
            plt.yticks(rotation=15)
            # plt.title("Association Rule Confidence Heatmap", fontsize=28)
            plt.tight_layout()

        return plt.gcf()

    def generate_heatmap2(self):
        matrix_1 = []
        for antecedent, consequent, confidence in self.matrix:
            antecedent_str = ', '.join(antecedent)
            consequent_str = ', '.join(consequent)
            matrix_1.append((antecedent_str, consequent_str, confidence))

        itemset_elements = []
        for itemset in matrix_1:
            ele = list(itemset)
            if ele[0] in reaction_words and ele[1] in reaction_words:
                continue
            if ele[0].endswith('K') and ele[1].endswith('K'):
                continue
            else:
                itemset_elements.append(ele)

        itemset_elements2 = []
        for itemset3 in itemset_elements:
            ele = list(itemset3)
            if ele[0].endswith('K') and ele[1] in reaction_words:
                continue
            else:
                itemset_elements2.append(ele)

        association_confidences = {}

        for antecedent, consequent, confidence in itemset_elements2:
            association_confidences[(frozenset(antecedent), consequent)] = confidence

        # 创建热图数据矩阵
        unique_antecedents = set()
        unique_consequents = set()

        for antecedent, consequent, confidence in itemset_elements2:
            unique_antecedents.add(antecedent)
            unique_consequents.add(consequent)

        antecedents = sorted(list(unique_antecedents), key=lambda x: str(x))
        consequents = sorted(list(unique_consequents), key=lambda x: str(x))
        data_for_heatmap = np.zeros((len(antecedents), len(consequents)))

        for i, antecedent in enumerate(antecedents):
            for j, consequent in enumerate(consequents):
                antecedent_set = frozenset(antecedent)
                confidence = association_confidences.get((antecedent_set, consequent), 0)
                data_for_heatmap[i, j] = confidence

        plt.ion()
        if data_for_heatmap.size == 0:
            plt.figure(figsize=(12, 12))
            plt.text(0.5, 0.5, "No valid data associations under set conditions!",
                     fontsize=14, ha='center', va='center')
            plt.axis('off')  # 隐藏坐标轴
        else:
            custom_cmap = LinearSegmentedColormap.from_list("custom",
                                                            ['#E8F4F5', '#D3EAED', '#A6D5DB',
                                                             '#A6DBC6', '#7C9FA4'])
            sns.set()
            plt.figure(figsize=(12, 12))
            ax = sns.heatmap(data_for_heatmap, cmap=custom_cmap, xticklabels=[str(c) for c in consequents],
                             yticklabels=antecedents, linewidths=1, cbar=True, cbar_kws={"pad": 0.15,
                                                                                         # 'orientation': 'horizontal',
                                                                                         },
            # sns.set()
            # plt.figure(figsize=(12, 12))
            # ax = sns.heatmap(data_for_heatmap, cmap='bwr', xticklabels=[str(c) for c in consequents],
            #                  yticklabels=antecedents, linewidths=1, cbar=True, cbar_kws={"pad": 0.15,
            #                                                                              # 'orientation': 'horizontal',
            #                                                                              },
                             # annot_kws={"size": 20}
                             )
            ax.set_xlabel("Consequent", fontsize=34)
            ax.set_ylabel("Antecedent", fontsize=34)
            ax.tick_params(axis='x', labelsize=30)
            ax.tick_params(axis='y', labelsize=30)
            plt.xticks(rotation=75)
            plt.yticks(rotation=90)
            # plt.title("Association Rule Confidence Heatmap", fontsize=28)
            plt.tight_layout()

        return plt.gcf()