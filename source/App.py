import pyautogui
import time
from ActionRecorder import MouseButton, MouseAction, ActionRecorder
import sys
from PySide6 import QtCore, QtWidgets, QtGui

# Will work on the actual widget later, just nice to know that for now it works.
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.B_Record = QtWidgets.QPushButton("Record")
        self.B_Action = QtWidgets.QPushButton("Playback")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.B_Record)
        self.layout.addWidget(self.B_Action)

        self.B_Action.clicked.connect(self.perform_clicks)
        self.B_Record.clicked.connect(self.Record)
        
    @QtCore.Slot()
    def perform_clicks(self):
        # Simulate clicks at random positions
        pyautogui.PAUSE = 2.5
        positions = [(100, 100), (200, 200), (300, 300)]  # Add more positions as needed
        for pos in positions:
            pyautogui.click(pos[0], pos[1])
       
    @QtCore.Slot()     
    def Record(self): 
        recorder = ActionRecorder()

        # print("Press 'R' to start recording and 'S' to stop recording.")
        # print("Press 'P' to play back the recorded actions.")

        while True:
            key = keyboard.read_event(suppress=True).name

            if key == "r":
                recorder.start_recording()
                print("Recording... Press 'S' to stop.")
            elif key == "s":
                recorder.stop_recording()
                print("Recording stopped.")
            elif key == "p":
                print("Playing back recorded actions...")
                recorder.playback()
                print("Playback complete.")
            elif key == "m":
                recorder.stop_recording
                break
        
        return recorder
        
        
if __name__ == "__main__":
    
    # Code to make the widget show
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
    
    # ClickEvent = MouseAction(100, 100, MouseButton.LEFT)
    # ClickEvent.DebugPrint()
    
    # # Code to record one click
    # OneClickRecorder = ActionRecorder()
    # print("Recording next click")
    # OneClickRecorder.StartRecording()

    # pyautogui.PAUSE = 2.5
    # time.sleep(10)
    # pyautogui.click(OneClickRecorder.RecordedAction.x, OneClickRecorder.RecordedAction.y)
    # print("Done")
    
    