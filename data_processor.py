import re
from Temperature_Substrate import extract_temperature, extract_substrate
# from Product_form import Product_Form
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

            # product_form_instance = Product_Form()
            # converted_words = product_form_instance.process_data_file(file_path)
            # if converted_words is not None:
            #     result_dict["Product_Form"] = converted_words
            # else:
            #     result_dict["Product_Form"] = set()

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

# if __name__ == "__main__":
#    data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]
#    results = process_data_files(data_files)
#
#    for result in results:
#        # print("Data File:", result["Data File"])
#        # print("Reaction:", result["Reaction"])
#        print("Temperature:", result["Temperature"])
#        print("Element:", result["Element"])
#        #print("Compounds:", result["Compounds"])
#        print("Substrate:", result["Substrate"])
#        print("Product_From:", result["Product_Form"])
#        print("Precursors:", result["Precursors"])
#        print("Reactions:", result["Reactions"])
#        print("Products:", result["Products"])
