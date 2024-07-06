from gpt4all import GPT4All
import PyPDF2
from PyPDF2 import PdfReader
import pandas as pd
import nlp_knowledge
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import re

nlp = spacy.load("en_core_web_sm")

def add_embedding_and_cosine_similarity(df, fixed_text):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    df['content_embedding'] = df['content'].apply(lambda x: model.encode(x, convert_to_tensor=True))
    fixed_text_embedding = model.encode(fixed_text, convert_to_tensor=True)
    df['similarity'] = df['content_embedding'].apply(lambda x: cosine_similarity([x.numpy()], [fixed_text_embedding.numpy()])[0][0])
    return df

def select_top_neighbors(df):
    df = df.sort_values('similarity', ascending=False)
    top_neighbors = df.head(10)
    return top_neighbors


def save_df_to_text(df_filtered, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for index, row in df_filtered.iterrows():
            file.write(row['content'] + '\n\n')  # Writing content and a blank line