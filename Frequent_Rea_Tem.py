import os
import re
from Compounds import find_words
from Reactions import reaction
from Fre_Tem_total import convert_to_K
from element_definitions import temperature_words
import matplotlib.pyplot as plt
import math

class FrequentReaTem:
    def __init__(self):
        data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]
        self.temperature_results = []
        self.reactions = []
        for file_path in data_files:
            with open(file_path, "r", encoding="utf-8") as file:
                paragraph = file.read()
                pattern = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
                cleaned_paragraph = re.sub(pattern, '', paragraph)
                paragraph = cleaned_paragraph

                temperature_pattern = r"\b\d+(?:\.\d+)?\s*(?:{})\b".format("|".join(temperature_words))
                paragraph = re.sub(temperature_pattern, convert_to_K, paragraph)
                result_tem = find_words(paragraph)
                temperature_set = result_tem["temperature"]
                temperature = {temp.replace(" ", "") for temp in temperature_set}
                self.temperature_results.append(temperature)

                result_rea = reaction(paragraph)
                reactions = len(result_rea)  # 统计反应的数量
                self.reactions.append(reactions)

    def plot_results(self):
        plt.figure(figsize=(10, 6))
        for temperature_set, reaction_count in zip(self.temperature_results, self.reactions):
            temperature_ranges = [f"{i}-{i + 100}" for i in range(0, 1000, 100)]
            temperature_counts = [0] * len(temperature_ranges)
            for temp in temperature_set:
                temp_value = float(temp.replace('K', ''))
                index = math.ceil(temp_value / 100) - 1
                if 0 <= index < len(temperature_counts):  # 确保 index 在有效范围内
                    temperature_counts[index] += 1
                else:
                    print(f"Temperature {temp} is out of range.")
            colors = ['#A6D5DB', '#EAA9C1', '#FACABC', '#C0BFDF', '#CCDCAD', '#F3A17C', '#AFACB7', '#f4cccc', '#ef8787',
                      '#f9b9b9', '#d68d8d', '#DBA6D5', '#A6DBC6', '#D5DBA6', '#7C9FA4', '#D3EAED', '#E8F4F5', '#DBC6A6']
            plt.bar(temperature_ranges, temperature_counts, color=colors)
        plt.xlabel('Temperature Range (K)', fontsize=18)
        plt.ylabel('Number of Reactions', fontsize=18)
        plt.title('Number of Reactions in Different Temperature Ranges', fontsize=20)
        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(rotation=0, fontsize=10)
        plt.show()

# 使用示例
frequent_reactions = FrequentReaTem()
frequent_reactions.plot_results()

#
# # 实例化 FrequentReaTem 类
# frequent_reactions = FrequentReaTem()
#
# # 绘制柱状图
# frequent_reactions.plot_results()




# import os
# import re
# from Compounds import find_words
# from Reactions import reaction
# from Fre_Tem_total import convert_to_K
# from element_definitions import temperature_words
# import matplotlib.pyplot as plt
#
# class FrequentReaTem:
#     def __init__(self):
#         data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]
#         temperature_results = []
#         all_transactions = []
#         for file_path in data_files:
#             with open(file_path, "r", encoding="utf-8") as file:
#                 paragraph = file.read()
#                 pattern = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
#                 cleaned_paragraph = re.sub(pattern, '', paragraph)
#                 paragraph = cleaned_paragraph
#
#                 temperature_pattern = r"\b\d+(?:\.\d+)?\s*(?:{})\b".format("|".join(temperature_words))
#                 paragraph = re.sub(temperature_pattern, convert_to_K, paragraph)
#                 result_tem = find_words(paragraph)
#                 temperature_set = result_tem["temperature"]
#                 temperature = {temp.replace(" ", "") for temp in temperature_set}
#                 temperature_results.append(temperature)
#
#                 result_rea = reaction(paragraph)
#                 reactions = result_rea
#
# plt.figure(figsize=(10, 6))
# plt.bar(temperature_results, reactions, color='blue')
# plt.xlabel('Temperature (K)')
# plt.ylabel('Number of Reactions')
# plt.title('Number of Reactions at Different Temperatures')
# plt.show()
