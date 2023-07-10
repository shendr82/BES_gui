# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:29:53 2023

@author: ShendR
"""
from PyQt5.QtCore import QPropertyAnimation, QRectF, QSize, Qt, pyqtProperty
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import (
    QAbstractButton,
    QApplication,
    QHBoxLayout,
    QSizePolicy,
    QWidget,
)


class Switch(QAbstractButton):
    def __init__(self, parent=None, track_radius=12, thumb_radius=6):
        super().__init__(parent=parent)
        self.setCheckable(True)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self._track_radius = track_radius
        self._thumb_radius = thumb_radius

        self._margin = max(0, self._thumb_radius - self._track_radius)
        self._base_offset = max(self._thumb_radius, self._track_radius)
        # self._end_offset = {
        #     True: lambda: self.width() - self._base_offset,
        #     False: lambda: self._base_offset,
        # }
        self._end_offset = {
            True: lambda: 65,
            False: lambda: 15,
        }
        # self._offset = self._base_offset
        self._offset = 10

        palette = self.palette()
        if self._thumb_radius > self._track_radius:
            self._track_color = {
                True: palette.dark(),
                False: palette.dark(),
            }
            self._thumb_color = {
                True: palette.shadow(),
                False: palette.light(),
            }
            self._text_color = {
                True: palette.highlightedText().color(),
                False: palette.dark().color(),
            }
            self._thumb_text = {
                True: 'Core',
                False: 'Edge',
            }
            self._track_opacity = 0.5
        else:
            self._thumb_color = {
                True: palette.highlightedText(),
                False: palette.light(),
            }
            self._track_color = {
                True: palette.highlight(),
                False: palette.dark(),
            }
            self._text_color = {
                True: palette.highlight().color(),
                False: palette.dark().color(),
            }
            self._thumb_text = {
                True: 'Edge',
                False: 'Core',
            }
            self._track_opacity = 1
        

    @pyqtProperty(int)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.update()

    def sizeHint(self):  # pylint: disable=invalid-name
        return QSize(
            12 * self._track_radius + 2 * self._margin,
            2 * self._track_radius + 2 * self._margin,
        )

    def setChecked(self, checked):
        super().setChecked(checked)
        self.offset = self._end_offset[checked]()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.offset = self._end_offset[self.isChecked()]()
        # self.offset = 100

    def paintEvent(self, event):  # pylint: disable=invalid-name, unused-argument
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setPen(Qt.NoPen)
        track_opacity = self._track_opacity
        thumb_opacity = 1.0
        text_opacity = 1.0
        if self.isEnabled():
            # track_brush = self._track_color[self.isChecked()]
            # thumb_brush = self._thumb_color[self.isChecked()]
            # text_color = self._text_color[self.isChecked()]
            track_brush = QColor(58, 59, 61)
            thumb_brush = QColor(52, 62, 72)
            text_color = QColor(250, 203, 63)
        else:
            track_opacity *= 0.8
            # track_brush = self.palette().shadow()
            # thumb_brush = self.palette().mid()
            # text_color = self.palette().shadow().color()
            track_brush = QColor(58, 59, 61)
            thumb_brush = QColor(52, 62, 72)
            text_color = QColor(250, 203, 63)
    
        p.setBrush(track_brush)
        p.setOpacity(track_opacity)
        p.drawRoundedRect(
            # 4,4,                                         # x, y position of track
            # 80,11,                                       # x, y size 
            # 6,6                                          # roundednes
            self._margin,
            self._margin,
            self.width() - 2 * self._margin,
            self.height() - 2 * self._margin,
            self._track_radius,
            self._track_radius,
        )
        p.setBrush(thumb_brush)
        p.setOpacity(thumb_opacity)
        p.drawRect(
            # 0, 0,                                    # x, y position of thumb 
            # 50, 20                                   # x, y size
            self.offset - self._thumb_radius,
            self._base_offset - self._thumb_radius,
            4 * self._thumb_radius,
            2 * self._thumb_radius,
        )
        p.setPen(text_color)
        p.setOpacity(text_opacity)
        font = p.font()
        font.setPixelSize(16)                                  # Text size
        # font.setPixelSize(2 * self._thumb_radius)
        p.setFont(font)
        p.drawText(
            QRectF(
                # 4, 1,                                   # position ???
                # 40, 15                                  # x, y rectangle size
                self.offset - self._thumb_radius,
                self._base_offset - self._thumb_radius,
                4 * self._thumb_radius,
                2 * self._thumb_radius,
            ),
            Qt.AlignCenter,
            self._thumb_text[self.isChecked()],
        )

    def mouseReleaseEvent(self, event):  # pylint: disable=invalid-name
        super().mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            anim = QPropertyAnimation(self, b'offset', self)
            anim.setDuration(120)
            # anim.setStartValue(10)
            # anim.setEndValue(100)
            anim.setStartValue(self.offset)
            anim.setEndValue(self._end_offset[self.isChecked()]())
            anim.start()

    def enterEvent(self, event):  # pylint: disable=invalid-name
        self.setCursor(Qt.PointingHandCursor)
        super().enterEvent(event)


def main():
    app = QApplication([])

    # Thumb size < track size (Gitlab style)
    s1 = Switch()
    # s1.isChecked()
    s1.toggled.connect(lambda c: print('toggled', c))
    s1.clicked.connect(lambda c: print('clicked', c))
    s1.pressed.connect(lambda: print('pressed'))
    s1.released.connect(lambda: print('released'))
    s2 = Switch()
    s2.setEnabled(False)
    # s1.checked == True

    # Thumb size > track size (Android style)
    s3 = Switch(thumb_radius=11, track_radius=8)
    # s3.setChecked(True)
    s4 = Switch(thumb_radius=11, track_radius=8)
    s4.setEnabled(False)

    l = QHBoxLayout()
    l.addWidget(s1)
    l.addWidget(s2)
    l.addWidget(s3)
    l.addWidget(s4)
    w = QWidget()
    w.setLayout(l)
    w.show()

    app.exec()


if __name__ == '__main__':
    main()
