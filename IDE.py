import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class SimpleIDE(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Text editor
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        # Buttons
        self.load_button = QPushButton('Load File')
        self.load_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_button)

        self.save_button = QPushButton('Save File')
        self.save_button.clicked.connect(self.save_file)
        self.layout.addWidget(self.save_button)

        self.execute_button = QPushButton('Run Code')
        self.execute_button.clicked.connect(self.run_code)
        self.layout.addWidget(self.execute_button)

        # Window settings
        self.setWindowTitle('Simple IDE')
        self.setGeometry(100, 100, 800, 600)

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Python Files (*.py);;All Files (*)')
        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit.setPlainText(file.read())

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Python Files (*.py);;All Files (*)')
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())

    def run_code(self):
        # Save current code to a temporary file
        temp_file = 'temp_code.py'
        with open(temp_file, 'w') as file:
            file.write(self.text_edit.toPlainText())

        # Execute the code
        try:
            exec(open(temp_file).read(), globals())
        except Exception as e:
            print(f"Error running code: {e}")

        # Clean up temporary file
        os.remove(temp_file)

def main():
    app = QApplication(sys.argv)
    editor = SimpleIDE()
    editor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

