from data_processor import process_data_files
import os
import re
import numpy as np
import seaborn as sns
from itertools import combinations
import matplotlib.pyplot as plt
from Compounds import find_words
from Product_form import Product_Form
from element_definitions import element_definitions
from element_definitions import Product_form

class AprioriEleProFor:
    def __init__(self):
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

                product_form_instance = Product_Form()
                product_form = product_form_instance.process_data_file(file_path)

                result_ele = find_words(paragraph)
                element = result_ele["element"]
                element_results.append(element)

                combined_set = set(element) | set(product_form) #| set(substrate) | set(reactions) | set(precursors) | set(products)
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
                        # if confidence >= min_confidence:
                        #     association_rules.append((antecedent_set, consequent, confidence))
            return matrix

        min_support = 80
        frequent_itemsets = apriori_analysis(all_transactions, min_support)
        self.matrix = generate_association_rules(frequent_itemsets)

        # element_results_list = [list(item) for item in element_results]
        # temperature_results_list = [list(item) for item in temperature_results]
        # matrix = generate_association_rules(frequent_itemsets)
        #
        # element_results_list = [list(item) for item in element_results]
        # temperature_results_list = [list(item) for item in temperature_results]

    def generate_heatmap(self):
        matrix_1 = []
        for antecedent, consequent, confidence in self.matrix:
            antecedent_str = ', '.join(antecedent)
            consequent_str = ', '.join(consequent)
            matrix_1.append((antecedent_str, consequent_str, confidence))

        itemset_elements = []
        for itemset in matrix_1:
            ele = list(itemset)
            if ele[0] in element_definitions and ele[1] in element_definitions:
                continue
            if ele[0] in Product_form and ele[1] in Product_form:
                continue
            # if ele[0] in Product_form2 and ele[1] in Product_form2:
            #     continue
            else:
                itemset_elements.append(ele)

        association_confidences = {}

        # 计算关联规则的置信度并存储在字典中
        for antecedent, consequent, confidence in itemset_elements:
            association_confidences[(frozenset(antecedent), consequent)] = confidence

        # 创建热图数据矩阵
        unique_antecedents = set()
        unique_consequents = set()

        for antecedent, consequent, confidence in itemset_elements:
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

        # 绘制热图
        sns.set()
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(data_for_heatmap, annot=True, cmap='YlGnBu', xticklabels=[str(c) for c in consequents],
                         yticklabels=antecedents,
                         annot_kws={"size": 12})
        ax.set_xlabel("Consequent", fontsize=16)
        ax.set_ylabel("Antecedent", fontsize=16)
        ax.tick_params(axis='x', labelsize=14)
        ax.tick_params(axis='y', labelsize=14)
        plt.xticks(rotation=15)
        plt.yticks(rotation=0)
        plt.title("Association Rule Confidence Heatmap", fontsize=18)

        # odd_indices = [i for i in range(len(itemset_elements)) if i % 2 == 1]
        # even_indices = [i for i in range(len(itemset_elements)) if i % 2 == 0]
        #
        # odd_data = [itemset_elements[i] for i in odd_indices]
        # even_data = [itemset_elements[i] for i in even_indices]
        #
        # fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        #
        # for data, ax in zip([odd_data, even_data], axes):
        #     directed_graph = nx.DiGraph()
        #
        #     # 添加节点时设置节点的颜色属性
        #     for idx, item in enumerate(data):
        #         element1, element2, confidence = item
        #         directed_graph.add_node(element1, color='lightblue')
        #         directed_graph.add_node(element2, color='lightblue')
        #         directed_graph.add_edge(element1, element2, weight=confidence, color='gray')
        #
        #     pos = nx.spring_layout(directed_graph)  # 设置随机数种子, seed=42
        #
        #     # 提取置信度大于0.85的数据
        #     high_confidence_data = [(element1, element2, confidence) for (element1, element2, confidence) in data if
        #                             float(confidence) > 0.85]
        #     low_confidence_data = [(element1, element2, confidence) for (element1, element2, confidence) in data if
        #                            float(confidence) <= 0.85]
        #
        #     # 更新节点和边的颜色属性
        #     for element1, element2, _ in high_confidence_data:
        #         directed_graph.nodes[element1]['color'] = '#FFCCCC'
        #         directed_graph.nodes[element2]['color'] = '#FFCCCC'
        #         directed_graph.edges[element1, element2]['color'] = '#FF9999'
        #
        #     # 绘制节点和边，根据颜色属性设置颜色
        #     nx.draw(directed_graph, pos, ax=ax, with_labels=True, # font_weight='bold',
        #             node_color=[directed_graph.nodes[node]['color'] for node in directed_graph.nodes()],
        #             edge_color=[directed_graph.edges[edge]['color'] for edge in directed_graph.edges()], node_size=1500,
        #             font_size=10)# connectionstyle='arc3, rad = 0.3'
        #
        #     # 绘制置信度大于0.85的边和标注数字
        #     edge_labels = {(element1, element2): f"{confidence:.2f}" for (element1, element2, confidence) in
        #                    high_confidence_data}
        #     nx.draw_networkx_edge_labels(directed_graph, pos, edge_labels=edge_labels, ax=ax, font_size=10)
        #
        #     # 绘制置信度小于0.85的边和标注数字
        #     edge_labels = {(element1, element2): f"{confidence:.2f}" for (element1, element2, confidence) in
        #                    low_confidence_data}
        #     nx.draw_networkx_edge_labels(directed_graph, pos, edge_labels=edge_labels, ax=ax, font_size=10)
        #
        #     ax.set_title("Element VS Products Form")
        #
        # plt.tight_layout()
        return plt.gcf()