from PySide2.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QDialogButtonBox, QFileDialog
from PySide2.QtCore import Qt

class ResultsDialog(QDialog):
    def __init__(self, results, headers=None):
        super().__init__()
        self.setWindowTitle("Table Data")
        self.setGeometry(400, 300, 990, 550)
        layout = QVBoxLayout(self)

        if headers is None:
            headers = []
        elif isinstance(headers, str):
            headers = [headers]
        num_columns = len(headers)
        self.table = QTableWidget(len(results), num_columns)
        self.table.setHorizontalHeaderLabels(headers)
        for row, result in enumerate(results):
            for col, header in enumerate(headers):
                text = ", ".join(result.get(header, []))
                item = QTableWidgetItem(text)
                item.setTextAlignment(Qt.AlignCenter)
                item.setTextAlignment(Qt.TextWordWrap)
                self.table.setItem(row, col, item)
                self.table.item(row, col).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.table.item(row, col).setToolTip(item.text())

        self.table.resizeRowsToContents()
        layout.addWidget(self.table)

        button_box = QDialogButtonBox(QDialogButtonBox.Save)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.save_table_data)

    def save_table_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Table Data", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)
        if file_path:
            with open(file_path, 'w', encoding='utf-8-sig') as file:
                headers = [self.table.horizontalHeaderItem(col).text() for col in range(self.table.columnCount())]
                file.write(','.join(headers) + '\n')
                for row in range(self.table.rowCount()):
                    row_data = []
                    for col in range(self.table.columnCount()):
                        item = self.table.item(row, col)
                        text = item.text()
                        if ',' in text:
                            text = f'"{text}"'
                        row_data.append(text)
                    file.write(','.join(row_data) + '\n')