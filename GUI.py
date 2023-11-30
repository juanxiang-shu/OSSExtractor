import sys
import os
from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget, QFileDialog, QSplitter, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QStackedWidget, QFrame,\
    QMessageBox
from PySide2.QtCore import Qt, QMimeData, QSize
from PySide2.QtGui import QDragEnterEvent, QDropEvent, QTextCursor, QColor, QFontMetrics, QPalette, QFont
from pdf import PDFProcessor
from statistics import Statistics
from selenium.webdriver.common.by import By
from blank_page import BlankPage
from analysis import Analysis
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import traceback


class DragDropWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pdf_processor = PDFProcessor()
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.implicitly_wait(10)
        # logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

    def initUI(self):
        self.setWindowTitle("OSSExtractor")
        self.setGeometry(500, 400, 800, 600)
        self.setStyleSheet("background-color: #f3f6f7;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QHBoxLayout(self.central_widget)

        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_width = 200
        left_widget.setMinimumWidth(left_width)
        left_widget.setMaximumWidth(left_width)

        self.read_button = QPushButton("Reader")
        self.read_button.setStyleSheet(
            "QPushButton {background-color: #84a7af; color: white; border: 2px solid #F4F1EA; "
            "border-radius: 18px; padding: 10px 20px;"
            "font-family: Arial; font-size: 18px; font-weight: bold;}"
            "QPushButton:hover {background-color: #AFACB7;}"
            "QPushButton:pressed {color: #afdde7;}"
        )
        left_layout.addWidget(self.read_button)
        self.read_button.clicked.connect(self.on_read_content_button_clicked)

        # Read Content button
        self.read_content_button = QPushButton("Read Content")
        self.read_content_button.setStyleSheet("QPushButton { color: #84a7af; font-family: Arial; font-size: 18px;"
                                               "background-color: #dde8e7; border: 2px solid #F4F1EA; "
                                               "border-radius: 18px; padding: 10px 20px;}")
        left_layout.addWidget(self.read_content_button)
        self.read_content_button.clicked.connect(self.read_and_extract)

        # Extract button
        self.extract_button = QPushButton("Extractor")
        self.extract_button.setStyleSheet(
            "QPushButton {background-color: #84a7af; color: white; border: 2px solid #F4F1EA; "
            "border-radius: 18px; padding: 10px 20px;"
            "font-family: Arial; font-size: 18px; font-weight: bold;}"
            "QPushButton:hover {background-color: #AFACB7;}"
            "QPushButton:pressed {color: #afdde7;}"
        )
        left_layout.addWidget(self.extract_button)
        self.extract_button.clicked.connect(self.on_extract_button_clicked)

        # Statistics button
        self.statistics_button = QPushButton("Statistics")
        self.statistics_button.setStyleSheet(
            "QPushButton {background-color: #84a7af; color: white; border: 2px solid #F4F1EA; "
            "border-radius: 18px; padding: 10px 20px;"
            "font-family: Arial; font-size: 18px; font-weight: bold;}"
            "QPushButton:hover {background-color: #AFACB7;}"
            "QPushButton:pressed {color: #afdde7;}"
        )
        left_layout.addWidget(self.statistics_button)
        self.statistics_button.clicked.connect(self.on_statistics_button_clicked)

        self.analysis_button = QPushButton("Analysis")
        self.analysis_button.setStyleSheet(
            "QPushButton {background-color: #84a7af; color: white; border: 2px solid #F4F1EA; "
            "border-radius: 18px; padding: 10px 20px;"
            "font-family: Arial; font-size: 18px; font-weight: bold;}"
            "QPushButton:hover {background-color: #AFACB7;}"
            "QPushButton:pressed {color: #afdde7;}"
        )
        left_layout.addWidget(self.analysis_button)
        self.analysis_button.clicked.connect(self.on_analysis_button_clicked)

        splitter.addWidget(left_widget)

        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        self.stacked_widget = QStackedWidget()
        right_layout.addWidget(self.stacked_widget)

        self.text_edit = QPlainTextEdit()
        self.text_edit.setStyleSheet("QPlainTextEdit { font-family: Arial; font-size: 18px; "
                                     "background-color: white; border: none; margin: 0; padding: 0;}")
        self.text_edit.setPlaceholderText(
            "Please enter the official URL of the scientific literature or drag the PDF or txt file")
        right_layout.addWidget(self.text_edit)
        self.stacked_widget.addWidget(self.text_edit)

        self.statistics = Statistics(self.text_edit, self.stacked_widget)
        self.stacked_widget.addWidget(self.statistics)

        self.blank_page = BlankPage(self.text_edit, self.stacked_widget)
        self.stacked_widget.addWidget(self.blank_page)

        self.analysis = Analysis(self.text_edit, self.stacked_widget)
        self.stacked_widget.addWidget(self.analysis)

        splitter.addWidget(right_widget)



    def get_next_data_file(self):
        i = 1
        while os.path.exists(f"data{i}.txt"):
            i += 1
        return f"data{i}.txt"

    def extract_text_and_save(self, path, driver):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        # self.chrome_options = Options()
        # # self.chrome_options.add_argument('--headless')
        # # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        # # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        # self.driver = webdriver.Chrome(options=self.chrome_options)

        try:
            driver.get(path)
            domain = driver.current_url.split('/')[2]

            if 'nature.com' in domain:
                elements = driver.find_element(By.CLASS_NAME, 'main-content')
                paragraphs = elements.find_elements(By.TAG_NAME, 'p')
                extracted_text1 = '\n'.join(element.text for element in paragraphs if element.text.strip())
                if extracted_text1:
                    txt_file_path = self.get_next_data_file()
                    with open(txt_file_path, 'w', encoding='utf-8') as file:
                        file.write(extracted_text1)
            elif 'acs.org' in domain:
                elements = driver.find_elements(By.CLASS_NAME, 'NLM_p')
                if not elements:
                    parent_div = WebDriverWait(driver, 100).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'article_content-left')))
                    elements = parent_div.find_elements(By.TAG_NAME, 'p')
                extracted_text2 = '\n'.join(element.text for element in elements if element.text.strip())
                if extracted_text2:
                    txt_file_path = self.get_next_data_file()
                    with open(txt_file_path, 'w', encoding='utf-8') as file:
                        file.write(extracted_text2)
            elif 'rsc.org' in domain:
                parent_div = WebDriverWait(driver, 100).until(
                    EC.presence_of_element_located((By.ID, 'pnlArticleContent'))
                )
                elements = parent_div.find_elements(By.TAG_NAME, 'p')
                extracted_text3 = '\n'.join(element.text for element in elements if element.text.strip())
                if extracted_text3:
                    txt_file_path = self.get_next_data_file()
                    with open(txt_file_path, 'w', encoding='utf-8') as file:
                        file.write(extracted_text3)
            elif 'wiley.com' in domain:
                elements = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'article__body'))
                )
                # elements = driver.find_element(By.CLASS_NAME, 'article__body')
                paragraphs = elements.find_elements(By.TAG_NAME, 'p')
                extracted_text4 = '\n'.join(element.text for element in paragraphs if element.text.strip())
                if extracted_text4:
                    txt_file_path = self.get_next_data_file()
                    with open(txt_file_path, 'w', encoding='utf-8') as file:
                        file.write(extracted_text4)
            elif 'science.org' in domain:
                element = WebDriverWait(driver, 100).until(
                    EC.presence_of_element_located((By.ID, 'bodymatter'))
                )
                paragraphs = element.find_elements(By.CSS_SELECTOR, 'div[role="paragraph"]')
                extracted_text5 = '\n'.join(paragraph.text for paragraph in paragraphs if paragraph.text.strip())

                if extracted_text5:
                    txt_file_path = self.get_next_data_file()
                    with open(txt_file_path, 'w', encoding='utf-8') as file:
                        file.write(extracted_text5)
        except Exception as e:
            print(f"Error extracting and saving text: {e}")
        except Exception as e:
            print(f"Error extracting and saving text: {e}")
            traceback.print_exc()
        finally:
            driver.quit()

    def read_and_extract(self):
        text_edit_content = self.text_edit.toPlainText()
        paths = self.pdf_processor.extract_path(text_edit_content).strip().split("\n")
        success_count = 0
        failure_count = 0

        for path in paths:
            if path.startswith("http://") or path.startswith("https://"):
                self.extract_text_and_save(path, self.driver)
            elif path.startswith("file:///"):
                pdf_file_path = path[8:]  # Remove "file:///"
                if self.pdf_processor.pdf_to_txt(pdf_file_path):
                    success_count += 1
                else:
                    failure_count += 1

        self.driver.quit()

        if failure_count == 0:
            QMessageBox.information(self, "Read Result", "Read successfully!")
        else:
            QMessageBox.critical(self, "Read Result", "Read failed!")

    def on_extract_button_clicked(self):
        self.stacked_widget.setCurrentWidget(self.blank_page)

    def on_read_content_button_clicked(self):
        self.stacked_widget.setCurrentWidget(self.text_edit)

    def on_statistics_button_clicked(self):
        self.stacked_widget.setCurrentWidget(self.statistics)

    def on_analysis_button_clicked(self):
        self.stacked_widget.setCurrentWidget(self.analysis)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        mime_data: QMimeData = event.mimeData()
        if mime_data.hasUrls():
            file_paths = [url.toLocalFile() for url in mime_data.urls()]
            file_contents = []
            for file_path in file_paths:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents.append(file.read())
            self.text_edit.setPlainText("\n".join(file_contents))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            text_cursor = self.text_edit.textCursor()
            if text_cursor.hasSelection():
                text_cursor.removeSelectedText()
            else:
                text_cursor.movePosition(QTextCursor.PreviousCharacter)
                text_cursor.deleteChar()
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyleSheet(style_sheet)
    window = DragDropWindow()
    window.show()
    sys.exit(app.exec_())
