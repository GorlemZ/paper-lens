import sys
import os
import logging
from pathlib import Path

# Set up logging
def setup_logging():
    if getattr(sys, 'frozen', False):
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
        # Import PyQt5 instead of Tkinter
        from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QMessageBox
        from PyQt5.QtCore import Qt
        
        logging.info("Creating main window")
        
        app = QApplication(sys.argv)
        
        window = QMainWindow()
        window.setWindowTitle("Paper Lens")
        window.resize(800, 600)
        
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
        
        # Add a button
        count = 0
        label = QLabel(f"Clicks: {count}")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18pt;")
        layout.addWidget(label) 

        def on_button_click():
            nonlocal count
            count += 1
            label.setText(f"Clicks: {count}")
        
        button = QPushButton("Click Me!")
        button.clicked.connect(on_button_click)
        layout.addWidget(button)
        
        # Add status information
        status = QLabel(f"Log file: {log_path}")
        status.setAlignment(Qt.AlignCenter)
        layout.addWidget(status)
        
        # Set central widget
        window.setCentralWidget(central_widget)
        
        # Show the window
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