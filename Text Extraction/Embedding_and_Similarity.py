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

def process_text_file_for_embedding(file_path):
    # read and process text
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
        fixed_text = (
            "The new COF was fabricated by first synthesizing two square planar tetratopic building blocks (5,10,15,20-tetrakis(4-aminophenyl)porphyrin (TAPP) and 5,10,15,20-tetrakis(4-formylphenyl)porphyrin (TFPP))."
            "5-(4-bromophenyl)-10,15,20-triphenylporphyrin (Br-TPP) and 4-isocyano-1,1′-biphenyl (ICBP) were selected as the precursors for the on-surface reaction on Au(111)."
            "The synthesis of single-layer COF-420 was carried out on a Au(111) surface in ultrahigh vacuum (UHV). TFPP molecules were first deposited onto the surface via thermal evaporation, followed by deposition of TAPP molecules. The adsorbed precursors were then gradually annealed to 180 °C and held at that temperature for 45 min to induce the condensation reaction that results in imine bond formation (Figure 1a). Figure 1b shows an STM topographic image of the resulting single-layer COF-420."
            "After the successive deposition of Br6-B10, ICBP and Pd and annealing at 403 K for 1 h, dendrimer 4 with 12 symmetrical antennae was generated on Au(111) surface."
        )
        df_with_embeddings = add_embedding_and_cosine_similarity(df, fixed_text)
        df_top_neighbors = select_top_neighbors(df_with_embeddings)

        base_name = os.path.basename(file_path)
        new_name = 'Embedding_' + base_name.replace('Processed_', '')
        output_file_path = os.path.join(os.path.dirname(file_path), new_name)
        save_df_to_text(df_top_neighbors, output_file_path)

    return output_file_path
