# import re
#
# compounds_words = {
#     "Bromo", "Chloro", "Fluoro", "Anisole", "Tetrahydrofuran", "oxane", "Acetal", "dimethyl alcohol", "boxylic acid"
# }
#
# # 构建正则表达式模式
# compound_pattern = r"\b(?:\S+\s+)*?(?:{})\s*\S*\b".format("|".join(map(re.escape, compounds_words)))
#
# your_text_here = '5,14-dibromo-1,10-dimethyldibenzo[a,m]rubicene, 1,10-dimethyldibenzo[a,m]rubicene 1,10-dimethyldibenzo[a,m]rubicene as the core motif with additional anthracene moieti 2,6-naphthalene-dicarboxylic acid'
#
# # 在文本中查找匹配项
# matches = re.findall(compound_pattern, your_text_here, re.IGNORECASE)
# print(matches)


# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl"}
#
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words1))
#
# compound_pattern2 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(map(re.escape, compounds_words2)))
#
# #your_text_here = '5,14-dibromo-1,10-dimethyldibenzo[a,m]rubicene, 1,10-dimethyldibenzo[a,m]rubicene 1,10-dimethyldibenzo[a,m]rubicene as the core motif with additional anthracene moieti 2,6-naphthalene-dicarboxylic acid ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol)'
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
#
# matches2 = []
# words = your_text_here.split()
# for i in range(len(words)):
#     if re.match(compound_pattern2, words[i], re.IGNORECASE):
#         matches2.append(words[i])
#
# all_matches = set(matches1 + matches2)
#
# print(all_matches)

# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(map(re.escape, compounds_words1)))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b(\S*(?:{})\S*)\b".format("|".join(map(re.escape, compounds_words2)))
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# all_matches = set(matches1 + matches2)
#
# print(all_matches)


# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(map(re.escape, compounds_words1)))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b(\S*(?:{})\S*)\b".format("|".join(map(re.escape, compounds_words2)))
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# complete_compounds = set()
#
# for match in matches1 + matches2:
#     if '(' in match and ')' in match:
#         complete_compounds.add(match)
#
# print(complete_compounds)


# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(map(re.escape, compounds_words1)))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b(\S*(?:{})\S*)\b".format("|".join(map(re.escape, compounds_words2)))
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# complete_compounds = set()
#
# for match in matches1 + matches2:
#     if '(' in match and ')' in match:
#         complete_compounds.add(match)
#     else:
#         complete_compounds.add(match)
#
# print(complete_compounds)


# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(map(re.escape, compounds_words1)))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b(\S*(?:{})\S*)\b".format("|".join(map(re.escape, compounds_words2)))
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# complete_compounds = set()
#
# for match in matches1 + matches2:
#     if '(' in match and ')' in match:
#         complete_compounds.add(match)
#     else:
#         # 判断字符串的前35个字符是否相同
#         existing_matches = [existing for existing in complete_compounds if existing[:35] == match[:35]]
#         if not existing_matches:
#             complete_compounds.add(match)
#         else:
#             # 如果存在相同前缀的元素，保留较长的元素
#             existing_match = existing_matches[0]
#             if len(match) > len(existing_match):
#                 complete_compounds.remove(existing_match)
#                 complete_compounds.add(match)
#
# print(complete_compounds)

# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(map(re.escape, compounds_words1)))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b(\S*(?:{})\S*)\b".format("|".join(map(re.escape, compounds_words2)))
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# complete_compounds = set()
#
# for match in matches1 + matches2:
#     # 去掉括号
#     match_without_brackets = re.sub(r'[(){}\[\]]', '', match)
#
#     if '(' in match and ')' in match and match_without_brackets:
#         complete_compounds.add(match)
#     else:
#         # 判断字符串的前35个字符是否相同
#         existing_matches = [existing for existing in complete_compounds if existing[:35] == match_without_brackets[:35]]
#         if not existing_matches:
#             complete_compounds.add(match)
#         else:
#             # 如果存在相同前缀的元素，保留较长的元素
#             existing_match = existing_matches[0]
#             if len(match) > len(existing_match):
#                 complete_compounds.remove(existing_match)
#                 complete_compounds.add(match)
#
# print(complete_compounds)

# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(map(re.escape, compounds_words1)))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b(\S*(?:{})\S*)\b".format("|".join(map(re.escape, compounds_words2)))
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# complete_compounds = set()
#
# for match in sorted(matches1 + matches2, key=len, reverse=True):
#     # 去掉括号
#     match_without_brackets = re.sub(r'[(){}\[\]]', '', match)
#
#     if '(' in match and ')' in match and match_without_brackets:
#         existing_matches = [existing for existing in complete_compounds if existing[:35] == match_without_brackets[:35]]
#         if not existing_matches or len(match) >= len(existing_matches[0]):
#             complete_compounds.difference_update(existing_matches)
#             complete_compounds.add(match)
#     else:
#         # 判断字符串的前35个字符是否相同
#         existing_matches = [existing for existing in complete_compounds if existing[:35] == match_without_brackets[:35]]
#         if not existing_matches:
#             complete_compounds.add(match)
#         else:
#             # 如果存在相同前缀的元素，保留较长的元素
#             existing_match = existing_matches[0]
#             if len(match) >= len(existing_match):
#                 complete_compounds.discard(existing_match)
#                 complete_compounds.add(match)
#
# print(complete_compounds)

# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words1))
# # compound_pattern2 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words2))
# compound_pattern2 = r"\b\s*([^ ]*(?:{}|{}))[^ ]*\b".format("|".join(compounds_words2), "|".join([re.escape('('), re.escape(')'), re.escape(','), re.escape('['), re.escape(']'), re.escape('-')]))
#
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = []
# for word in your_text_here.split():
#     match_result = re.match(compound_pattern2, word, re.IGNORECASE)
#     print(f"Word: {word}, Match: {match_result}")
#     if match_result:
#         matches2.append(word)
#
# # matches2 = [word for word in your_text_here.split() if re.match(compound_pattern2, word, re.IGNORECASE)]
#
# all_matches = set(matches1 + matches2)
#
# # Remove brackets and check for completeness
# def remove_brackets(compound):
#     return re.sub(r'[()]', '', compound)
#
# # Sort by length
# sorted_matches = sorted(all_matches, key=lambda x: len(remove_brackets(x)), reverse=True)
#
# # Filter based on completeness and longest prefix
# complete_compounds = set()
# for match in sorted_matches:
#     match_without_brackets = remove_brackets(match)
#     if not any(existing_without_brackets[:35] == match_without_brackets[:35] for existing_without_brackets in complete_compounds):
#         complete_compounds.add(match_without_brackets)
#
# print(complete_compounds)

# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words1))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b\s*(\S*(?:{}|{}))[^ ]*\b".format(
#     "|".join(compounds_words2),
#     "|".join([re.escape('('), re.escape(')'), re.escape(','), re.escape('['), re.escape(']'), re.escape('-')])
# )
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# all_matches = set(matches1 + matches2)
#
# # Remove brackets and check for completeness
# def remove_brackets(compound):
#     return re.sub(r'[()]', '', compound)
#
# # Sort by length
# sorted_matches = sorted(all_matches, key=lambda x: len(remove_brackets(x)), reverse=True)
#
# # Filter based on completeness and longest prefix
# complete_compounds = set()
# for match in sorted_matches:
#     match_without_brackets = remove_brackets(match)
#     if not any(existing_without_brackets.startswith(match_without_brackets) for existing_without_brackets in complete_compounds):
#         complete_compounds.add(match)
#
# print(complete_compounds)


# import re
#
# compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
# compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}
#
# # 构建不带空格的正则表达式模式
# compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words1))
#
# # 构建带有空格的正则表达式模式
# compound_pattern2 = r"\b(\S*(?:{}|{}))\S*\b".format(
#     "|".join(compounds_words2),
#     "|".join([re.escape('('), re.escape(')'), re.escape(','), re.escape('['), re.escape(']'), re.escape('-')])
# )
#
#
# your_text_here = 'Anthracene 1,10-dimethyldibenzo[a,m]rubicene oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'
#
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# all_matches = set(matches1 + matches2)
#
# # Remove brackets, special characters, and check for completeness
# def clean_and_check(compound):
#     cleaned_compound = re.sub(r'[\[\](),-]', '', compound)
#     return cleaned_compound
#
# # Sort by length
# sorted_matches = sorted(all_matches, key=lambda x: len(clean_and_check(x)), reverse=True)
#
# # Filter based on completeness and longest prefix
# complete_compounds = set()
# for match in sorted_matches:
#     match_cleaned = clean_and_check(match)
#     if not any(existing_cleaned.startswith(match_cleaned) for existing_cleaned in complete_compounds):
#         complete_compounds = {existing for existing in complete_compounds if not match_cleaned.startswith(existing)}
#         complete_compounds.add(match)
#
# print(complete_compounds)

import re

compounds_words1 = {"boxylic acid", "dimethyl alcohol"}
compounds_words2 = {"phenyl", "methyl", "biphenyl", "hydroxymethyl"}

# 构建不带空格的正则表达式模式
compound_pattern1 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words1))

# 构建带有空格的正则表达式模式，确保匹配完整的单词
compound_pattern2 = r"\b\s*(\S*(?:{})\S*)\s*\b".format("|".join(compounds_words2))
# compound_pattern2 = r"\b(\S*(?:{}))\b".format("|".join(map(re.escape, compounds_words2)))

your_text_here = '(5,10,15,20-tetrakis(4-aminophenyl)porphyrin 5,10,15,20-tetrakis(4-formylphenyl)porphyrin Anthracene 1,10-dimethyldibenzo[a,m]aminophenyl oligomers with diacetylene (4,4′-bis(hydroxymethyl)biphenyl) linkers were synthesized by annealing ([1,1′,3′,1′′,3′′,1′′′-quaterphenyl]-3,3′′′-dimethyl alcohol) at 400 K, we deduce that the mechanism involves a Cu atom catalyzing desilylation, and subsequently a hydrogen atom from the substrate or vacuum terminates the dissociated trimethylsilyl radical'

matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)

all_matches = set(matches1 + matches2)

# Remove brackets and check for completeness
# def remove_brackets(compound):
#     # 去除字符串开头的 "[" 或 "("
#     if compound.startswith('[') or compound.startswith('('):
#         compound = compound.lstrip('[').lstrip('(')
#     return compound
def remove_brackets(compound):
    # 去除字符串开头的 "[" 或 "("
    if compound.startswith('[') or compound.startswith('('):
        compound = compound.lstrip('[').lstrip('(')

    # 去除字符串结尾的 "[" 或 "("
    if compound.endswith(']') or compound.endswith(')'):
        compound = compound.rstrip(']').rstrip(')')

    return compound


# Sort by length
sorted_matches = sorted(all_matches, key=lambda x: len(remove_brackets(x)), reverse=True)

# Filter based on completeness and longest prefix
complete_compounds = set()
for match in sorted_matches:
    match_without_brackets = remove_brackets(match)
    if not any(existing_without_brackets[:35] == match_without_brackets[:35] for existing_without_brackets in complete_compounds):
        complete_compounds.add(match_without_brackets)

print(complete_compounds)
# matches1 = re.findall(compound_pattern1, your_text_here, re.IGNORECASE)
# matches2 = re.findall(compound_pattern2, your_text_here, re.IGNORECASE)
#
# all_matches = set(matches1 + matches2)
#
# # Remove brackets, special characters, and check for completeness
# def clean_and_check(compound):
#     cleaned_compound = re.sub(r'[\[\](),-]', '', compound)
#     return cleaned_compound
#
# # Sort by length
# sorted_matches = sorted(all_matches, key=lambda x: len(clean_and_check(x)), reverse=True)
#
# # Filter based on completeness and longest prefix
# complete_compounds = set()
# for match in sorted_matches:
#     match_cleaned = clean_and_check(match)
#     if not any(existing_cleaned.startswith(match_cleaned) for existing_cleaned in complete_compounds):
#         complete_compounds = {existing for existing in complete_compounds if not match_cleaned.startswith(existing)}
#         complete_compounds.add(match)
#
# print(complete_compounds)














