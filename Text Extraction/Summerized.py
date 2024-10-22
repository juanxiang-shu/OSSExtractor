from gpt4all import GPT4All
import pandas as pd
import os

def Model_3(df):
    summarized = []
    for index, row in df.iterrows():
        content = row['content']
        prompt_template_for_summarize_text = (
            f"{content}\n"            
            f"Task: Please summarize the following details in a table: precursor molecules, substrates, annealing/reaction temperature of the molecules, products (i.e., the compound molecules formed in this experiment), and the dimensionality of the product molecules (Simplified numbers plus letters). If no information is provided or you are unsure, use N/A. Please focus on extracting experimental conditions only from the surface chemistry synthesis. The table should have 5 columns: | Precursor | Substrate | Temperature | Products | Dimensions |"
        )
        model = GPT4All('nous-hermes-llama2-13b.Q4_0.gguf', allow_download=False) 
        summarize_text = model.generate(prompt=prompt_template_for_summarize_text, max_tokens=250, temp=0.0, top_p=0.6)
        print("summarize_text:")        
        summarized.append(summarize_text)
    df['summarized'] = pd.Series(summarized)

    return df

def save_df_to_text(df_filtered, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for index, row in df_filtered.iterrows():
            file.write(row['summarized'] + '\n\n')
