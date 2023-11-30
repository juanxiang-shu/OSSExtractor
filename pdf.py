import os
from pdfminer.high_level import extract_text
import re

class PDFProcessor:
    def __init__(self):
        pass

    def extract_path(self, text_edit_content):
        path = text_edit_content.strip()
        return path

    @staticmethod
    def process_pdfminer_text(pdfminer_text):
        lines = pdfminer_text.split('\n')
        processed_lines = []
        temp_line = ""

        for line in lines:
            line = line.strip()
            if len(line) > 0:
                if temp_line and temp_line.endswith('-'):
                    temp_line = temp_line.rstrip('-')
                    temp_line += line
                elif temp_line and not temp_line.endswith(('。', '？', '！', '.', '?', '!')):
                    temp_line += ' ' + line
                else:
                    temp_line += line

        if temp_line:
            processed_lines.append(temp_line)

        processed_lines = [line for line in processed_lines if len(re.findall(r'\b\w+\b', line)) > 5]

        processed_text = ' '.join(processed_lines)

        return processed_text

    def pdf_to_txt(self, pdf_file_path):
        try:
            with open(pdf_file_path, 'rb') as pdf_file:
                text = extract_text(pdf_file)
                text = self.process_pdfminer_text(text)

                txt_file_path = self.get_next_data_file()
                with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text)
                return True
        except Exception as e:
            print(f"Error converting {pdf_file_path}: {e}")
            return False

    def get_next_data_file(self):
        i = 1
        while True:
            file_name = f"data{i}.txt"
            if not os.path.exists(file_name):
                return file_name
            i += 1
