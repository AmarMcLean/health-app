import sys
from reminder_widget import ReminderClass
from scheduler import timer
from PySide6.QtWidgets import QApplication

# Create qt class app with console input
app = QApplication(sys.argv)
# Start main app loop
app.exec()
