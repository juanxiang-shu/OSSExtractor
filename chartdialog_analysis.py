from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class ChartDialogA(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = None
        self.setWindowTitle("Analysis")

        layout = QVBoxLayout(self)

        # 创建一个 matplotlib 图形画布，并添加到布局中
        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)

        # 创建一个保存按钮，并连接到保存图像的方法
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_image)

    def set_figure(self, figure):
        self.figure = figure
        self.update_canvas()

    def update_canvas(self):
        if self.figure:
            self.canvas.figure = self.figure
            self.canvas.draw()

    def save_image(self):
        if self.figure:
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_path, _ = file_dialog.getSaveFileName(self, "Save Chart", "", "SVG (*.SVG);;"
                                                        "PNG Image (*.png);;JPEG Image (*.jpg);;"
                                                          "TIF Image (*.tif);;PDF File (*.pdf);;"
                                                          "BMP File (*.bmp)")

            if file_path:
                self.figure.savefig(file_path, bbox_inches='tight')
                self.figure.savefig(file_path, dpi=600)

class ChartDialogB(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = None
        self.setWindowTitle("Analysis")

        layout = QVBoxLayout(self)

        # 创建一个 matplotlib 图形画布，并添加到布局中
        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)

        # 创建一个保存按钮，并连接到保存图像的方法
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_image)

    def set_figure(self, figure):
        self.figure = figure
        self.update_canvas()

    def update_canvas(self):
        if self.figure:
            self.canvas.figure = self.figure
            self.canvas.draw()

    def save_image(self):
        if self.figure:
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_path, _ = file_dialog.getSaveFileName(self, "Save Chart", "", "SVG (*.SVG);;"
                                                        "PNG Image (*.png);;JPEG Image (*.jpg);;"
                                                          "TIF Image (*.tif);;PDF File (*.pdf);;"
                                                          "BMP File (*.bmp)")

            if file_path:
                self.figure.savefig(file_path, bbox_inches='tight')
                self.figure.savefig(file_path, dpi=600)

