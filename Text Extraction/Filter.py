from gpt4all import GPT4All
import PyPDF2
import pandas as pd
import nlp_knowledge
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os


def Model_1(df):
    model = GPT4All('nous-hermes-llama2-13b.Q4_0.gguf', allow_download=False)
    questions = [
        "Question: Does this section cover the types of surface chemical reactions or experimental studies on the formation of molecules on surfaces? Answer 'Yes' or 'No'. \nAnswer:"
    ]

    for idx, row in df.iterrows():
        content = row['content']
        classification = 'No'
        for question in questions:
            prompt = f"{content}\n{question}"
            print(prompt)
            response = model.generate(prompt=prompt)
            first_word_of_response = response.split()[0].replace('.', '').replace(',', '')
            print(first_word_of_response)
            if first_word_of_response not in ['No', 'Not']:
                classification = first_word_of_response
                break
        df.loc[idx, 'classification'] = classification

    condition = (df['classification'] != 'No') & (df['classification'] != 'Not')
    df_filtered = df[condition]
    return df_filtered

def save_df_to_text(df_filtered, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for index, row in df_filtered.iterrows():
            file.write(row['content'] + '\n\n')  # Writing content and a blank line

def process_text_file_for_filter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    current_segment = []
    segments = []
    for line in lines:
        if line.strip():
            current_segment.append(line.strip())
        else:
            if current_segment:
                segments.append(' '.join(current_segment))
                current_segment = []
    if current_segment:
        segments.append(' '.join(current_segment))

    df = pd.DataFrame(segments, columns=['content'])
    df_filtered = Model_2(df)

    base_name = os.path.basename(file_path)
    # Remove 'Processed_' prefix and add 'Embedding_' prefix
    new_name = 'Filter_' + base_name.replace('Embedding_', '')
    output_file_path = os.path.join(os.path.dirname(file_path), new_name)
    save_df_to_text(df_filtered, output_file_path)

    return output_file_path
