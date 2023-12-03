from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QFileDialog

class ChartDialogS(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chart")
        self.layout = QVBoxLayout(self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.save_button = QPushButton("Save")
        self.layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_chart)

    def save_chart(self):
        file_dialog = QFileDialog(self, "Save Chart", "", "PNG Image (*.png);;JPEG Image (*.jpg);;"
                                                          "TIF Image (*.tif);;PDF File (*.pdf);;"
                                                          "BMP File (*.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.figure.savefig(file_path, dpi=600)
