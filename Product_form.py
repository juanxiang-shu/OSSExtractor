from element_definitions import Product_form
from collections import Counter
# 显示一个
class Product_Form:
    def __init__(self):
        pass
    def process_data_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            paragraph = file.read()
            word0 = paragraph.split()

            word_counts = Counter()
            for word in word0:
                word = word.strip(".,!?").lower()
                for category, keywords in Product_form.items():
                    if any(keyword.lower() in word for keyword in keywords):
                        word_counts[category] += 1

            most_common_category = word_counts.most_common(1)
            most_common_category = [(category, count) for category, count in most_common_category if count > 1]

            matched_categories = set()

            for category, _ in most_common_category:
                matched_categories.add(category)

            return matched_categories

product_form_instance = Product_Form()

# 两个都可以显示
# from collections import Counter
#
# class Product_Form:
#     def __init__(self):
#         pass
#
#     def process_data_file(self, file_path):
#         with open(file_path, "r", encoding="utf-8") as file:
#             paragraph = file.read()
#             word0 = paragraph.split()
#
#             word_counts = Counter()
#             for word in word0:
#                 word = word.strip(".,!?").lower()
#                 for category, keywords in Product_form.items():
#                     if any(keyword.lower() in word for keyword in keywords):
#                         word_counts[category] += 1
#
#             most_common_categories = word_counts.most_common(2)
#
#             if len(most_common_categories) >= 2:
#                 max_count, second_max_count = most_common_categories[0][1], most_common_categories[1][1]
#                 difference = max_count - second_max_count
#
#                 if difference <= 3:
#                     matched_categories = {category for category, _ in most_common_categories}
#                 else:
#                     matched_categories = {most_common_categories[0][0]}
#             else:
#                 matched_categories = set()
#
#             return matched_categories
#
# # Example usage:
# product_form_instance = Product_Form()




