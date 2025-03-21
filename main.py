import sys
import os
import logging
from pathlib import Path


# Set up logging
def setup_logging():
    if getattr(sys, "frozen", False):
        app_dir = Path(os.path.dirname(sys.executable))
    else:
        app_dir = Path(os.path.dirname(os.path.abspath(__file__)))

    log_path = app_dir / "paper_lens.log"
    logging.basicConfig(filename=str(log_path), level=logging.DEBUG)
    return log_path


# Main application
def main():
    log_path = setup_logging()
    logging.info("Application starting")

    try:
        # Import PyQt5
        from PyQt5.QtWidgets import QApplication, QMessageBox
        from app.interface import MainWindow

        app = QApplication(sys.argv)

        # Create and show the main window
        window = MainWindow(log_path)
        window.show()

        logging.info("GUI components created, starting main loop")

        # Start the event loop
        sys.exit(app.exec_())

    except Exception as e:
        logging.error(f"Error in main: {e}", exc_info=True)
        print(f"CRITICAL ERROR: {str(e)}")
        print(f"See log for details: {log_path}")


if __name__ == "__main__":
    main()
