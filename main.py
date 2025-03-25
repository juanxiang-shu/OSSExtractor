import pandas as pd
import os
import PDF_to_TXT
from TXT_Processing import process_text_file_for_processing
from Embedding_and_Similarity import process_text_file_for_embedding
from Filter import process_text_file_for_filter
from Abstract import process_text_file_for_abstract
from Summerized import process_text_file_for_summerized

pdf_files = [
'path/your/file_1',...'path/your/file_n'
]
base_output_dir = 'path/your/folder'  
output_files = PDF_to_TXT.save_contents_to_specific_folders(pdf_files, base_output_dir)

total_filtered_count = 0

for file_path in pdf_files:
    processed_file_path, filtered_count = process_text_file_for_processing(file_path)
    total_filtered_count += filtered_count

print("Total filtered count:", total_filtered_count)

for file_path in output_files:# output_files:
    print(file_path)
    processed_file_path = process_text_file_for_processing(file_path)
    embedding_file_path = process_text_file_for_embedding(processed_file_path)
    filter_file_path = process_text_file_for_filter(embedding_file_path)
    abstract_file_path = process_text_file_for_abstract(file_path)
    summerized_file_path = process_text_file_for_summerized(file_path)



