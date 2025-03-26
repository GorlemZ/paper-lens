from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
)
from PyQt6.QtCore import pyqtSignal


class CSVInputComponent(QWidget):
    file_selected = pyqtSignal(str)  # Signal to emit when file is selected

    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_file_path = None
        self.setup_ui()

    def setup_ui(self):
        # Create horizontal layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        # Create file path input field
        self.file_path_input = QLineEdit()
        self.file_path_input.setReadOnly(True)
        self.file_path_input.setPlaceholderText("Select a CSV file...")
        layout.addWidget(self.file_path_input)

        # Create browse button
        self.browse_button = QPushButton("Browse CSV")
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        # Create upload button
        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.upload_file)
        self.upload_button.setEnabled(False)  # Disabled until file is selected
        layout.addWidget(self.upload_button)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv);;All Files (*.*)"
        )

        if file_path:
            self.selected_file_path = file_path
            self.file_path_input.setText(file_path)
            self.upload_button.setEnabled(
                True
            )  # Enable upload button when file is selected

    def upload_file(self):
        if self.selected_file_path:
            self.file_selected.emit(self.selected_file_path)
            self.upload_button.setEnabled(False)  # Disable after upload
        else:
            QMessageBox.warning(self, "Upload Error", "Please select a file first.")
