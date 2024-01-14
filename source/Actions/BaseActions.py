from enum import Enum, auto
from dataclasses import dataclass

# Enum for mouse button clicks. Can be expanded in future to include middle, forward, backward (if enabled on mouse).
class MouseButton(Enum):
    LEFT = auto()
    RIGHT = auto()

# Dataclass for individual mouse input events.
# TODO when you have more actions, make BaseAction class to use as interface
@dataclass
class MouseAction:
    x: int
    y: int
    button: MouseButton
    
    def __init__(self, x: int, y: int, button: MouseButton):
        self.x = x
        self.y = y
        self.button = button
    
    def DebugPrint(self):
        print(f"X: {self.x}, Y: {self.y}, Button: {self.button.name}")