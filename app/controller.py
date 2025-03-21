import logging
from pathlib import Path
from PyQt5.QtCore import QObject, pyqtSlot
from app.logic.file_manager import FileManager
from app.logic.spacy_task import extract_keys
from pandas import DataFrame


class Controller(QObject):
    def __init__(self):
        super().__init__()
        self.file_manager = FileManager()

    @pyqtSlot(str)
    def handle_file_selection(self, file_path: str) -> None:
        """
        Handle the file selection event from the UI.
        Args:
            file_path (str): Path to the selected file
        """
        if self.file_manager.set_file(file_path):
            logging.info(f"File successfully loaded: {file_path}")
        else:
            logging.error(f"Failed to load file: {file_path}")

    def start_computation(self) -> None:
        """
        Handle the computation start event from the UI.
        Args:
            start (str): Start signal
        """
        try:
            df: DataFrame = self.file_manager.read_file()
            logging.info(f"Read {df.size} lines from file.")
            results = extract_keys(df)
        except Exception as e:
            logging.error(f"Failed to start computation: {e}")
