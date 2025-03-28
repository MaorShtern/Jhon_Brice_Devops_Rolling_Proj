import logging
import json



class JSONFormatter(logging.Formatter):
    def __init__(self, date_format='%d-%m-%Y %H:%M:%S'):
        super().__init__()
        self.date_format = date_format


    def format(self, record):
        log_message = {
            "asctime": self.formatTime(record, datefmt=self.date_format),
            "name": "main",  # Set name to "main"
            "levelname": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_message)
