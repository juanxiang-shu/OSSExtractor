from gpt4all import GPT4All
import pandas as pd
import os
import re
def Model_2(df):
    abstract = []
    for index, row in df.iterrows():
        content = row['content']

        prompt_template_for_abstract_text = (
            f"{content}"
            f"Answer the question as truthfully as possible using the provided context."
            f"Please summarize the text below, emphasizing the types of reactions featured in the author's scientific experiments on surface reactions."            
        )
        model = GPT4All('nous-hermes-llama2-13b.Q4_0.gguf', allow_download=False)
        abstract_text = model.generate(prompt=prompt_template_for_abstract_text, max_tokens=250, temp=0.0, top_p=0.6)
        print("abstract_text:")
        print(abstract_text)
        abstract.append(abstract_text)
    df['abstract'] = pd.Series(abstract)

    return df

def process_text_file_for_abstract(file_path):
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
    df_final = Model_2(df)

    base_name = os.path.basename(file_path)
    new_name = 'Abstract_' + base_name.replace('Filter_', '')
    output_file_path = os.path.join(os.path.dirname(file_path), new_name)
    save_df_to_text(df_final, output_file_path)
    return output_file_path
