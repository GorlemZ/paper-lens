from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
)
from PyQt5.QtCore import Qt
from .csv_input import CSVInputComponent
from ..controller import Controller
from app.logic.logger import QTextEditLogger
import logging
from PyQt5.QtCore import pyqtSignal


class MainWindow(QMainWindow):
    def __init__(self, log_path):
        """Initialize the main application window."""
        super().__init__()
        self.log_path = log_path
        self.count = 0
        self.controller = Controller()
        self.setup_ui()

        # Set up logging to QLabel
        logTextBox = QTextEditLogger(self.log_display)
        logTextBox.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.INFO)

    def setup_ui(self):
        """Set up the user interface components."""
        logging.info("Creating main window")

        self.setWindowTitle("Paper Lens")
        self.resize(800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Add title
        title = QLabel("Paper Lens")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24pt;")
        layout.addWidget(title)

        # Add info text
        info = QLabel("Welcome to Paper Lens!")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("font-size: 14pt;")
        layout.addWidget(info)

        # Add CSV input component
        self.csv_input = CSVInputComponent()
        self.csv_input.file_selected.connect(self.controller.handle_file_selection)
        layout.addWidget(self.csv_input)

        # Add start computation button
        start_button = QPushButton("Start Computation")
        start_button.setStyleSheet("font-size: 12pt;")
        layout.addWidget(start_button)
        # Connect start computation button to controller
        start_button.clicked.connect(self.controller.start_computation)

        # Add log text box
        self.log_display = QLabel("Logs will appear here...")
        self.log_display.setAlignment(Qt.AlignLeft)
        self.log_display.setStyleSheet(
            "background-color: #f0f0f0; padding: 10px; font-family: monospace;"
        )
        self.log_display.setWordWrap(True)
        layout.addWidget(self.log_display)

        # Set central widget
        self.setCentralWidget(central_widget)
