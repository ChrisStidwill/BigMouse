# Imports required to run PySide6 code (temporarily in this class)
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
from ..Widgets.MainWindowSidebar import VTabWidget

# The MainWindow consists of a vertical tab widget on the left which calls to a widget switcher on the right. All further
# functionality is handled by widgets in the widget switcher.
class MainWindow(QMainWindow):    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Create a central widget with your VTabWidget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        v_tab_widget = VTabWidget(central_widget)
        v_tab_widget.addTab(QWidget(), 'tab1')
        v_tab_widget.addTab(QWidget(), 'tab2')
        v_tab_widget.addTab(QWidget(), 'tab3')





    # Below is some old code kept for reference.

    #     self.B_Record = QtWidgets.QPushButton("Record")
    #     self.B_Action = QtWidgets.QPushButton("Playback")
    #     self.text = QtWidgets.QLabel("Hello World",
    #                                  alignment=QtCore.Qt.AlignCenter)

    #     self.layout = QtWidgets.QVBoxLayout(self)
    #     self.layout.addWidget(self.text)
    #     self.layout.addWidget(self.B_Record)
    #     self.layout.addWidget(self.B_Action)

    #     self.B_Action.clicked.connect(self.perform_clicks)
    #     self.B_Record.clicked.connect(self.Record)
        
    # @QtCore.Slot()
    # def perform_clicks(self):
    #     # Simulate clicks at random positions
    #     pyautogui.PAUSE = 2.5
    #     positions = [(100, 100), (200, 200), (300, 300)]  # Add more positions as needed
    #     for pos in positions:
    #         pyautogui.click(pos[0], pos[1])
       
    # @QtCore.Slot()     
    # def Record(self): 
    #     recorder = ActionRecorder()

    #     # print("Press 'R' to start recording and 'S' to stop recording.")
    #     # print("Press 'P' to play back the recorded actions.")

    #     while True:
    #         key = keyboard.read_event(suppress=True).name

    #         if key == "r":
    #             recorder.start_recording()
    #             print("Recording... Press 'S' to stop.")
    #         elif key == "s":
    #             recorder.stop_recording()
    #             print("Recording stopped.")
    #         elif key == "p":
    #             print("Playing back recorded actions...")
    #             recorder.playback()
    #             print("Playback complete.")
    #         elif key == "m":
    #             recorder.stop_recording
    #             break
        
    #     return recorder