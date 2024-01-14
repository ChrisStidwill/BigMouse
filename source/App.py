
import sys
from GUI.Screens.MainWindow import MainWindow
from PySide6 import QtWidgets

# Main app class that is run from main.
class App:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.widget = MainWindow()
        self.widget.resize(800, 600)
        
    def RunApp(self):
        self.widget.show()
        
        sys.exit(self.app.exec())

# Where the program is run.
if __name__ == "__main__":
    
    # Opens the Main Window of the app.
    AppInstance = App()
    AppInstance.RunApp()
    
    
    
    
    # Below is some old code kept for reference.
    
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
    
    