from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QCheckBox, QDialog, QMessageBox
from PySide2.QtGui import QPainter, QColor
from PySide2.QtCore import Qt
from results_dialog import ResultsDialog
from data_processor import process_data_files
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from chartdialog_analysis import ChartDialogA, ChartDialogB
from apriori_Rea_Tem import AprioriReaTem
from apriori_Rea_Sub import AprioriReaSub
from apriori_Tem_Sub import AprioriTemSub
import subprocess
import numpy as np
import xlrd
import os

class Analysis(QWidget):
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

        self.temperature_checkbox = QCheckBox("Temperature")
        self.temperature_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
                                                " color: white; border: 2px solid #F4F1EA;"
                                                " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                                "font-size: 18px; font-weight: bold;}"
                                                "QCheckBox:hover {background-color: #AFACB7;}")
        layout.addWidget(self.temperature_checkbox)

        self.substrate_checkbox = QCheckBox("Substrate")
        self.substrate_checkbox.setStyleSheet("QCheckBox {background-color: #3E6b83;"
                                              " color: white; border: 2px solid #F4F1EA;"
                                              " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                              "font-size: 18px; font-weight: bold;}"
                                              "QCheckBox:hover {background-color: #AFACB7;}")
        layout.addWidget(self.substrate_checkbox)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setStyleSheet("QPushButton {background-color: #3E6b83;"
                                          " color: white; border: 2px solid #F4F1EA;"
                                          " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                          "font-size: 18px; font-weight: bold;}"
                                          "QPushButton:hover {background-color: #AFACB7;}")
        self.confirm_button.clicked.connect(self.extract_and_process_data)
        layout.addWidget(self.confirm_button)

    def show_selection_error_dialog(self, message):
        error_dialog = QMessageBox(self)
        error_dialog.setWindowTitle("Error")
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.exec_()

    def extract_and_process_data(self):
        reactions_checked = self.reactions_checkbox.isChecked()
        substrate_checked = self.substrate_checkbox.isChecked()
        temperature_checked = self.temperature_checkbox.isChecked()
        
        selected_count = sum([reactions_checked, substrate_checked, temperature_checked,
                              ])
        if selected_count > 2:
            self.show_selection_error_dialog("Only two options can be selected!")
            return

        if reactions_checked and temperature_checked:
            apriori_reatem = AprioriReaTem()
            heatmap_figure = apriori_reatem.generate_heatmap1()

            chart_dialog = ChartDialogA(self)
            chart_dialog.set_figure(heatmap_figure)
            chart_dialog.show()

            heatmap_figure = apriori_reatem.generate_heatmap2()

            chart_dialog1 = ChartDialogB(self)
            chart_dialog1.set_figure(heatmap_figure)
            chart_dialog1.show()

        if reactions_checked and substrate_checked:
            apriori_reasub = AprioriReaSub()
            heatmap_figure = apriori_reasub.generate_heatmap1()

            chart_dialog = ChartDialogA(self)
            chart_dialog.set_figure(heatmap_figure)
            chart_dialog.show()

            heatmap_figure = apriori_reasub.generate_heatmap2()

            chart_dialog = ChartDialogA(self)
            chart_dialog.set_figure(heatmap_figure)
            chart_dialog.show()

        if temperature_checked and substrate_checked:
            apriori_temsub = AprioriTemSub()
            heatmap_figure = apriori_temsub.generate_heatmap1()

            chart_dialog = ChartDialogA(self)
            chart_dialog.set_figure(heatmap_figure)
            chart_dialog.show()

            heatmap_figure = apriori_temsub.generate_heatmap2()

            chart_dialog = ChartDialogA(self)
            chart_dialog.set_figure(heatmap_figure)
            chart_dialog.show()





