from PySide6.QtWidgets import QStyle, QTabWidget, QTabBar, QStylePainter, QStyleOptionTab, QWidget
from PySide6.QtCore import QSize, QRect, QPoint
from PySide6.QtGui import QPaintEvent

# VTabBar is a vertical tab widget 
class VTabBar(QTabBar):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def tabSizeHint(self, index: int) -> QSize:
        s = super().tabSizeHint(index)
        s.transpose()
        return s

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QStylePainter(self)
        opt = QStyleOptionTab()
        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QRect(QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt)
            painter.restore()

# VTabWidget is a vertical tab widget that sits west of the screen.
class VTabWidget(QTabWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setTabBar(VTabBar())
        self.setTabPosition(QTabWidget.West)