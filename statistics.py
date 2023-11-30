from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide2.QtCore import Qt
import matplotlib.pyplot as plt
from Fre_sub_total import sorted_words, process_data_sub
from Fre_rea_total import sorted_word1, process_data_rea
from Fre_profor_total import sorted_word2, process_data_pro
from Fre_Tem_total import converted_sorted_words, process_data_tem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from chartdialog_statistics import ChartDialogS

class Statistics(QWidget):
    def __init__(self, text_edit, stacked_widget):
        super().__init__()
        self.text_edit = text_edit
        self.stacked_widget = stacked_widget
        self.chart_dialog = None
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        self.choose_file_button = QPushButton("Reaction")
        self.choose_file_button.setStyleSheet("QPushButton {background-color: #3E6b83;"
                                              " color: white; border: 2px solid #F4F1EA;"
                                              " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                              "font-size: 18px; font-weight: bold;}"
                                              "QPushButton:hover {background-color: #AFACB7;}")
        layout.addWidget(self.choose_file_button)
        self.choose_file_button.clicked.connect(self.plot_chart_reaction)

        self.choose_file_button = QPushButton("Temperature")
        self.choose_file_button.setStyleSheet("QPushButton {background-color: #3E6b83;"
                                              " color: white; border: 2px solid #F4F1EA;"
                                              " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                              "font-size: 18px; font-weight: bold;}"
                                              "QPushButton:hover {background-color: #AFACB7;}")
        layout.addWidget(self.choose_file_button)
        self.choose_file_button.clicked.connect(self.plot_chart_temperature)

        self.choose_file_button = QPushButton("Substrate")
        self.choose_file_button.setStyleSheet("QPushButton {background-color: #3E6b83;"
                                              " color: white; border: 2px solid #F4F1EA;"
                                              " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                              "font-size: 18px; font-weight: bold;}"
                                              "QPushButton:hover {background-color: #AFACB7;}")
        layout.addWidget(self.choose_file_button)
        self.choose_file_button.clicked.connect(self.plot_chart_substrate)

        self.choose_file_button = QPushButton("Product Form")
        self.choose_file_button.setStyleSheet("QPushButton {background-color: #3E6b83;"
                                              " color: white; border: 2px solid #F4F1EA;"
                                              " font-family: Arial; border-radius: 18px; padding: 10px 20px;"
                                              "font-size: 18px; font-weight: bold;}"
                                              "QPushButton:hover {background-color: #AFACB7;}")
        layout.addWidget(self.choose_file_button)
        self.choose_file_button.clicked.connect(self.plot_chart_profor)

    def plot_chart_substrate(self):
        processed_data = process_data_sub(sorted_words)
        substrate_data, frequency_data = zip(*processed_data)
        self.figure.clear()
        self.figure.set_size_inches(9, 7)
        ax = self.figure.add_subplot(111)

        colors = ['#A6D5DB', '#EAA9C1', '#FACABC', '#C0BFDF', '#CCDCAD', '#F3A17C', '#AFACB7', '#f4cccc', '#ef8787',
                  '#f9b9b9', '#d68d8d', '#DBA6D5', '#A6DBC6', '#D5DBA6', '#7C9FA4', '#D3EAED', '#E8F4F5', '#DBC6A6']
        ax.pie(frequency_data, autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=1.1, textprops={'fontsize': 24})# labels=substrate_data,

        legend = ax.legend(substrate_data, loc='best', fontsize=26)
        legend.set_bbox_to_anchor((1, 1))

        ax.set_title('Substrate Distribution', fontsize=30)
        self.canvas.draw()
        if not self.chart_dialog:
            self.chart_dialog = ChartDialogS(self)
        self.chart_dialog.canvas.figure = self.figure
        self.chart_dialog.canvas.draw()
        self.chart_dialog.exec_()

    def plot_chart_temperature(self):
        interval = 100  # 定义温度区间
        temperature_ranges, frequencies = process_data_tem(converted_sorted_words, interval)
        temperature_data = temperature_ranges
        frequency_data = frequencies
        self.figure.clear()
        self.figure.set_size_inches(9, 7)
        ax = self.figure.add_subplot(111)

        colors = ['#A6D5DB', '#EAA9C1', '#FACABC', '#C0BFDF', '#CCDCAD', '#F3A17C', '#AFACB7', '#f4cccc', '#ef8787',
                  '#f9b9b9', '#d68d8d', '#DBA6D5', '#A6DBC6', '#D5DBA6', '#7C9FA4', '#D3EAED', '#E8F4F5', '#DBC6A6']
        ax.pie(frequency_data, autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=1.1, textprops={'fontsize': 24})#labels=temperature_data,
        legend = ax.legend(temperature_data, loc='best', fontsize=26)
        legend.set_bbox_to_anchor((1, 1))

        ax.set_title('Temperature Distribution', fontsize=30)
        self.canvas.draw()
        if not self.chart_dialog:
            self.chart_dialog = ChartDialogS(self)
        self.chart_dialog.canvas.figure = self.figure
        self.chart_dialog.canvas.draw()
        self.chart_dialog.exec_()

    def plot_chart_reaction(self):
        processed_data = process_data_rea(sorted_word1)
        reaction_data, frequency_data = zip(*processed_data)
        self.figure.clear()
        self.figure.set_size_inches(9, 7)
        ax = self.figure.add_subplot(111)

        colors = ['#A6D5DB', '#EAA9C1', '#FACABC', '#C0BFDF', '#CCDCAD', '#F3A17C', '#AFACB7', '#f4cccc', '#ef8787',
                  '#f9b9b9', '#d68d8d', '#DBA6D5', '#A6DBC6', '#D5DBA6', '#7C9FA4', '#D3EAED', '#E8F4F5', '#DBC6A6']
        ax.pie(frequency_data, autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=1.1,
               textprops={'fontsize': 22}) # labels=reaction_data,

        legend = ax.legend(reaction_data, fontsize=22, loc='best')
        legend.set_bbox_to_anchor((1, 1))

        ax.set_title('Reaction Distribution', fontsize=26)
        self.canvas.draw()
        if not self.chart_dialog:
            self.chart_dialog = ChartDialogS(self)
        self.chart_dialog.canvas.figure = self.figure
        self.chart_dialog.canvas.draw()
        self.chart_dialog.exec_()

    def plot_chart_profor(self):
        processed_data = process_data_pro(sorted_word2)
        profor_data, frequency_data = zip(*processed_data)
        self.figure.clear()
        self.figure.set_size_inches(9, 7)
        ax = self.figure.add_subplot(111)

        colors = ['#A6D5DB', '#EAA9C1', '#FACABC', '#C0BFDF', '#CCDCAD', '#F3A17C', '#AFACB7', '#f4cccc', '#ef8787',
                  '#f9b9b9', '#d68d8d', '#DBA6D5', '#A6DBC6', '#D5DBA6', '#7C9FA4', '#D3EAED', '#E8F4F5', '#DBC6A6']
        ax.pie(frequency_data, autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=1.1, textprops={'fontsize': 24})# , labels=profor_data,

        legend = ax.legend(profor_data, loc='best', fontsize=26)
        legend.set_bbox_to_anchor((1, 1))

        ax.set_title('Product Form Distribution', fontsize=30)
        self.canvas.draw()
        if not self.chart_dialog:
            self.chart_dialog = ChartDialogS(self)
        self.chart_dialog.canvas.figure = self.figure
        self.chart_dialog.canvas.draw()
        self.chart_dialog.exec_()









