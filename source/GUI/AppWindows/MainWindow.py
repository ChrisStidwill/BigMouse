# Imports required to run PySide6 code (temporarily in this class)
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QDockWidget
from PySide6.QtWidgets import QWidget
from ..Widgets.MainWindowSidebar import VTabWidget
from ..Widgets.RecordingScreen import RecordingScreenWidget

# The MainWindow consists of a vertical tab widget on the left which calls to a widget switcher on the right. All further
# functionality is handled by widgets in the widget switcher.
# TODO fix casing here, also around code base.
class MainWindow(QMainWindow):    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Create a central widget with your VTabWidget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Create an instance of RecordingScreenWidget and add it to the layout
        recordingScreenWidget = RecordingScreenWidget("Record Actions", central_widget)
        
        v_tab_widget = VTabWidget(central_widget)
        v_tab_widget.addTab(recordingScreenWidget, 'Record')
        v_tab_widget.addTab(QWidget(), 'tab2')
        v_tab_widget.addTab(QWidget(), 'tab3')
        
        # Example stylesheet to customize the appearance
        # v_tab_widget.setStyleSheet("""
        #     QTabWidget::pane {
        #         border: 1px solid #D0D0D0;
        #         border-top-left-radius: 4px;
        #         border-top-right-radius: 4px;
        #         background-color: #F5F5F5;
        #     }
        #     QTabWidget::tab-bar {
        #         left: 10px; /* move to the right by 10px */
        #     }
        #     QTabBar::tab {
        #         width: 40px; /* set the width of each tab */
        #         height: 120px; /* set the height of each tab */
        #         background-color: #F0F0F0;
        #         border: 1px solid #D0D0D0;
        #         border-bottom: none;
        #         border-top-left-radius: 4px;
        #         border-top-right-radius: 4px;
        #         padding: 5px;
        #         color: #444444;
        #         font-family: "Poppins", sans-serif;
        #     }
        #     QTabBar::tab:hover {
        #         background-color: #EEDC82; /* yellow undertone for hover and selected */
        #     }
        #     QTabBar::tab:selected{
        #         background-color: #D5B85A; /* yellow undertone for hover and selected */
        #     }
        #     QTabBar::tab:!selected {
        #         margin-top: 2px; /* move non-selected tabs down slightly */
        #     }
        # """)
        
        layout = QVBoxLayout(central_widget)
        layout.addWidget(v_tab_widget)



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