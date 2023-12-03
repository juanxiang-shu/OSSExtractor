import re
from Temperature_Substrate import extract_temperature, extract_substrate
from Precursors import extract_precursors
from Product import extract_products
from Reactions import reaction

def process_data_files(data_files):
    all_results = []
    for file_path in data_files:
        with open(file_path, "r", encoding="utf-8") as file:
            paragraph1 = file.read()
            pattern1 = r"(?<=\s)\(\d+(?:-\d+)?(?:,\d+)*\)(?=\s)"
            cleaned_paragraph1 = re.sub(pattern1, '', paragraph1)
            cleaned_paragraph = cleaned_paragraph1.strip()
            paragraph = cleaned_paragraph
            result_dict = {}

            temperature = extract_temperature(paragraph)
            result_dict["Temperatures"] = temperature

            substrate =extract_substrate(paragraph)
            result_dict["Substrates"] = substrate

            precursors = extract_precursors(paragraph)
            result_dict["Precursors"] = precursors

            reactions = reaction(paragraph)
            result_dict["Reactions"] = reactions

            products = extract_products(paragraph)
            result_dict["Products"] = products

            all_results.append(result_dict)

    return all_results
