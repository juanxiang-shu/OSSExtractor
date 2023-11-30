from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QCheckBox
from PySide2.QtGui import QPainter, QColor, QPen
from PySide2.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, QRect, QPointF
from results_dialog import ResultsDialog
from data_processor import process_data_files
from Product_form import Product_Form
import os

class BlankPage(QWidget):
    def __init__(self, text_edit, stacked_widget):
        super().__init__()
        self.text_edit = text_edit
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        self.reactions_checkbox = QCheckBox("Reactions")
        self.reactions_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
                                                " color: white; border: 2px solid #F4F1EA;"
                                                " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                                "font-size: 18px; font-weight: bold;}"
                                                "QCheckBox:hover {background-color: #AFACB7;}")
        layout.addWidget(self.reactions_checkbox)

        self.temperature_checkbox = QCheckBox("Temperatures")
        self.temperature_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
                                                " color: white; border: 2px solid #F4F1EA;"
                                                " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                                "font-size: 18px; font-weight: bold;}"
                                                "QCheckBox:hover {background-color: #AFACB7;}")
        layout.addWidget(self.temperature_checkbox)

        self.substrate_checkbox = QCheckBox("Substrates")
        self.substrate_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
                                                " color: white; border: 2px solid #F4F1EA;"
                                                " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                                "font-size: 18px; font-weight: bold;}"
                                                "QCheckBox:hover {background-color: #AFACB7;}")
        layout.addWidget(self.substrate_checkbox)

        self.precursors_checkbox = QCheckBox("Precursors")
        self.precursors_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
                                                " color: white; border: 2px solid #F4F1EA;"
                                                " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                                "font-size: 18px; font-weight: bold;}"
                                                "QCheckBox:hover {background-color: #AFACB7;}")
        layout.addWidget(self.precursors_checkbox)

        self.products_checkbox = QCheckBox("Products")
        self.products_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
                                                " color: white; border: 2px solid #F4F1EA;"
                                                " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                                "font-size: 18px; font-weight: bold;}"
                                                "QCheckBox:hover {background-color: #AFACB7;}")
        layout.addWidget(self.products_checkbox)

        # self.product_form_checkbox = QCheckBox("Product Form")
        # self.product_form_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
        #                                         " color: white; border: 2px solid #F4F1EA;"
        #                                         " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
        #                                         "font-size: 18px; font-weight: bold;}"
        #                                         "QCheckBox:hover {background-color: #AFACB7;}")
        # layout.addWidget(self.product_form_checkbox)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setStyleSheet("QPushButton {background-color: #3E6b83;"
                                          " color: white; border: 2px solid #F4F1EA;"
                                          " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                          "font-size: 18px; font-weight: bold;}"
                                          "QPushButton:hover {background-color: #AFACB7;}")
        self.confirm_button.clicked.connect(self.extract_and_process_data)
        layout.addWidget(self.confirm_button)

    def extract_and_process_data(self):
        reactions_checked = self.reactions_checkbox.isChecked()
        substrate_checked = self.substrate_checkbox.isChecked()
        temperature_checked = self.temperature_checkbox.isChecked()
        precursors_checked = self.precursors_checkbox.isChecked()
        # product_form_checked = self.product_form_checkbox.isChecked()
        products_checked = self.products_checkbox.isChecked()

        data_files = [f for f in os.listdir() if f.startswith('data') and f.endswith('.txt')]
        all_results = []

        for data_file in data_files:
            results = process_data_files([data_file])
            for result in results:
                result_dict = {}
                if reactions_checked:
                    result_dict['Reactions'] = result['Reactions']
                if temperature_checked:
                    result_dict['Temperatures'] = result['Temperatures']
                if precursors_checked:
                    result_dict['Precursors'] = result['Precursors']
                # if product_form_checked:
                #     product_form_instance = Product_Form()
                #     result_dict['Product_Form'] = product_form_instance.process_data_file(data_file)
                if products_checked:
                    result_dict['Products'] = result['Products']
                if substrate_checked:
                    result_dict['Substrates'] = result['Substrates']
                all_results.append(result_dict)

        headers = []
        if reactions_checked:
            headers.append('Reactions')
        if temperature_checked:
            headers.append('Temperatures')
        if precursors_checked:
            headers.append('Precursors')
        # if product_form_checked:
        #     headers.append('Product_Form')
        if products_checked:
            headers.append('Products')
        if substrate_checked:
            headers.append('Substrates')
        dialog = ResultsDialog(all_results, headers)
        dialog.exec_()