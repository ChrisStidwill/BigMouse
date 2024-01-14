from pynput.mouse import Listener as MouseListener
from Actions.BaseActions import MouseButton, MouseAction

# Recorder of different actions. 
# TODO this class won't scale well, need to revisit this when more actions can be recorded
class ActionRecorder:
    
    # Recorded action stored as this action. TODO this should be updated to a type of the base class (when it exists)
    RecordedAction: MouseAction
    
    # Listener for the action event.
    ActionListener = None
    
    def __init__(self):
        self.RecordedAction = None
        self.ActionListener = None

    # Records the click and ends recording. Is called by the ActionListener.
    def RecordClick(self, x, y, Button, pressed):
        if pressed:
           self.RecordedAction = MouseAction(x, y, MouseButton.LEFT)
           self.StopRecording()

    # To record a click action, call this function first.
    def StartRecording(self):
        self.ActionListener = MouseListener(on_click=self.RecordClick)
        self.ActionListener.start()

    def StopRecording(self):
        if self.ActionListener:
            self.ActionListener.stop()
        
        if self.RecordedAction:
            self.RecordedAction.DebugPrint()