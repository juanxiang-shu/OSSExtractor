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
