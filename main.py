from PyQt6.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget,)
app = QApplication([])
win = QWidget()


win.setWindowTitle('Okosho_ockoshnika')
win.resize(300,200)

text = QLabel("Hello world!")

line = QVBoxLayout()

line.addWidget(text)
line.addWidget(line)
win.setLayout(QVBoxLayout().addWidget(text))

win.show()

app.exec()