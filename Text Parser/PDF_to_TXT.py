import os
import PyPDF2
import nlp_knowledge

nlp = spacy.load("en_core_web_sm")


def process_page_text(page_text, max_tokens=200):
    doc = nlp(page_text)
    parts = []
    tokens_count = 0
    content = ""
    for sent in doc.sents:
        sent_tokens = len(list(sent))
        if tokens_count + sent_tokens > max_tokens and content:
            parts.append((content.strip(), tokens_count))
            content = ""
            tokens_count = 0
        content += sent.text + " "
        tokens_count += sent_tokens
    if content:
        parts.append((content.strip(), tokens_count))
    return parts


def save_contents_to_specific_folders(pdf_files, base_output_dir):
    output_paths = []
    for pdf in pdf_files:
        base_name = os.path.splitext(os.path.basename(pdf))[0]
        specific_output_dir = os.path.join(base_output_dir, base_name)
        os.makedirs(specific_output_dir, exist_ok=True)

        output_txt_filename = os.path.join(specific_output_dir, f"{base_name}.txt")
        with open(pdf, 'rb') as pdf_content:
            pdf_reader = PyPDF2.PdfReader(pdf_content)
            with open(output_txt_filename, 'w', encoding='utf-8') as output_file:
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    if page_text:
                        contents = process_page_text(page_text)
                        for content, _ in contents:
                            output_file.write(content + '\n\n')
        output_paths.append(output_txt_filename)

    return output_paths