from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

# TODO comments
# Also this should be an abstract class but can be used for now while testing.
class BaseScreenWidget(QWidget):
    def __init__(self, title, parent=None):
        super(BaseScreenWidget, self).__init__(parent)
        self.initUI(title)

    def initUI(self, title):
        # Create a QVBoxLayout for the ScreenWidget
        layout = QVBoxLayout(self)

        # Create a QLabel for the title
        title_label = QLabel(title, self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Add the title label to the layout
        layout.addWidget(title_label)

        # Add other widgets or content specific to the screen
        # For example, a QPushButton
        button = QPushButton("Click me!", self)
        layout.addWidget(button)

        # Set the layout for the ScreenWidget
        self.setLayout(layout)
