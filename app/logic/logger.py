import logging


class QTextEditLogger(logging.Handler):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.widget.setText("")

    def emit(self, record):
        msg = self.format(record)
        self.widget.setText(
            f"{self.widget.text()}\n{msg}" if self.widget.text() else msg
        )
