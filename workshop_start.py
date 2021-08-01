'''
This is a very basic PyQt5 window
It can be adapted to do anything
'''

import sys

from PyQt5 import QtGui
from PyQt5.QtOpenGL import *
from PyQt5 import QtCore, QtOpenGL, Qt
from PyQt5.QtWidgets import *

class MenuWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setMinimumSize(800,200)
    
        # setting window title
        self.setWindowTitle('no idea')
        self.setWindowIcon(QtGui.QIcon('utils/logo_icon.jpg'))
        
        # init layout
        self.layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # here is where you create your widgets and add them to the layout
        self.label = QLabel("nathacks is awesome!")
        self.layout.addWidget(self.label,0,0)
        self.label.setFont(QtGui.QFont('Arial',14))
        self.button = QPushButton('say hello')
        self.button.pressed.connect(lambda: self.hello(True))
        self.layout.addWidget(self.button, 1,0)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.count = 0

        self.space_presses = 0

    def update(self):
        self.count += 1
        print('count: {}'.format(self.count))

  
    def hello(self, caller):
        print('hello from the button')
        print('caller: {}'.format(caller))
        color = QInputDialog.getText(self,'dialog','give a color')[0]
        self.label2 = QLabel('this is ' +color)
        self.layout.addWidget(self.label2,1,1)
        self.label2.setStyleSheet("background-color: " + color + ";")

    def closeEvent(self, event):
        # this code will autorun just before the window closes
        print('this application is about to close')
        event.accept()
    
    def keyPressEvent(self, event):
        print('key event')
        if event.key() == QtCore.Qt.Key_Space:
            self.space_presses += 1
            self.label.setText('space presses: {}'.format(self.space_presses))
           

if __name__ == '__main__':       
    app = QApplication(sys.argv)     
    win = MenuWindow() 
    win.show() 
    sys.exit(app.exec())
    print('this line will never run because the previous line exited. If you want code to run later, change the previous line to just be app.exec()')