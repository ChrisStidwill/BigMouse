from ..Widgets.BaseScreen import BaseScreenWidget
from PySide6.QtWidgets import QComboBox, QWidget, QVBoxLayout

# The idea behind the recording screen widget is to have a screen where:
# A) New actions can be recorded based on certain types of actions.
# and eventually
# B) Entire recording can be done.

# To achieve this, we need this widget to interact with a recording manager.
# From that manager, it can send requests, and it can also send back the list of actions. That manager will be a singleton.


# Widget for the recording screen.
class RecordingScreenWidget(BaseScreenWidget):
    def __init__(self, title, parent: QWidget):
        super().__init__(title, parent)
        # self.initUI(self, title)
        
    def  initUI(self, title):
        
        print("Init")
        super().initUI(title)

        # Add a QComboBox
        combo_box = QComboBox()
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")
        
        # You can also connect a function to the currentIndexChanged signal
        combo_box.currentIndexChanged.connect(self.onComboBoxIndexChanged)
        
        # Add any additional configuration or styling for the QComboBox here
        # For example:
        # combo_box.setStyleSheet("background-color: white;")

        # Add the QComboBox to the layout or set its geometry as needed
        # For example, if you are using a QVBoxLayout:
        baseLayout = self.layout
        baseLayout.addWidget(combo_box)
        
        self.setLayout(baseLayout)

    def onComboBoxIndexChanged(self, index):
        # Handle the index change event here
        print(f"Selected index: {index}")
        
