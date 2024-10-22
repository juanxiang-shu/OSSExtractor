import PyPDF2
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load the English model of Spacy
nlp = spacy.load("en_core_web_sm")

def get_txt_from_pdf(pdf_file):
    data = []
    with open(pdf_file, 'rb') as pdf_content:
        pdf_reader = PyPDF2.PdfReader(pdf_content)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                words = page_text.split()
                page_text_join = ' '.join(words)
                page_len = len(page_text_join)
                div_len = page_len // 4

                page_parts = [page_text_join[i * div_len:(i + 1) * div_len] for i in range(4)]

                for i, page_part in enumerate(page_parts):
                    data.append({
                        'file name': pdf_file,
                        'page number': page_num + 1,
                        'page section': i + 1,
                        'content': page_part,
                        'tokens': len(nlp(page_part))
                    })
    return pd.DataFrame(data)

def preprocess_and_filter_text(df):
    pattern = r'(?i)\b(Acknowledgements|Acknowledgement|Data availability|References|Reference|Conflict of interest|Conflicts of interest|Conflict of interests|Conflicts of interests)\b'
    stop_processing = False
    last_valid_index = None

    for index, row in df.iterrows():
        # If you have decided to stop processing, exit the loop
        if stop_processing:
            break

        # Checks for the presence of the specified word and decides to stop further processing if found
        if re.search(pattern, row['content']):
            stop_processing = True
            cleaned_text = re.sub(pattern + r'[\s\S]*', '', row['content'])  # Clear the specified word and everything after it
            df.at[index, 'content'] = cleaned_text
            last_valid_index = index
        else:
            last_valid_index = index

    # If necessary, crop the DataFrame according to the last valid index
    if last_valid_index is not None:
        return df.iloc[:last_valid_index + 1]
    else:
        return df
