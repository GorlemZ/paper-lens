import logging
from pathlib import Path
import pandas as pd


class FileManager:
    def __init__(self):
        self._current_file_path = None

    @property
    def current_file_path(self) -> Path | None:
        return self._current_file_path

    def set_file(self, file_path: str) -> bool:
        try:
            path = Path(file_path)
            if not path.exists():
                logging.error(f"File does not exist: {file_path}")
                return False

            self._current_file_path = path
            logging.info(f"File path set to: {file_path}")
            return True
        except Exception as e:
            logging.error(f"Error setting file path: {e}")
            return False

    def read_file(self) -> list[str]:
        if self._current_file_path:
            try:
                return pd.read_csv(self._current_file_path)
            except Exception as e:
                logging.error(f"Error reading file: {e}")
        else:
            logging.error("No file path set.")
        return []
