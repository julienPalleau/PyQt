# https://stackabuse.com/working-with-pythons-pyqt-framework/
# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget
#
# # Create the Qt Application
# app = QApplication(sys.argv)
#
# # Create the parent widget
# window = QWidget()
#
# # Create the buttons
# button1 = QPushButton('One')
# button2 = QPushButton('Two')
# button3 = QPushButton('Three')
# button4 = QPushButton('Four')
# button5 = QPushButton('Five')
#
# # Create the QGrid Layout Manager
# layout = QGridLayout(window)
#
# # Add button Widgets to the QGridLqyout
# # addWidget([object], [row_number], [column number])
# layout.addWidget(button1,0,0)
# layout.addWidget(button2,1,0)
# layout.addWidget(button3,2,0)
# layout.addWidget(button4,0,1)
# layout.addWidget(button5,0,2)
#
# # Add a title
# window.setWindowTitle('A Simple PyQt6 App')
# # Set a default box at x=100, y=100 and 280 wide and 80 height
# window.setGeometry(100, 100, 280, 80)
#
# # Show the parent widget
# window.show()
#
# # Run the main Qt loop
# sys.exit(app.exec())

# ------------------------------------------

# # QFormLayout
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
#
#
# def addLabel(layout, text):
#     layout.addWidget(QLabel(text))
#
#
# # Create the Qt Application
# app = QApplication(sys.argv)
#
# # Create the parent Widget and the QVBoxLayout Layout Manager
# window = QWidget()
# layout = QVBoxLayout(window)
#
# # Create a label Widget and add it to the Layout
# label = QLabel('Enter some text!')
# layout.addWidget(label)
#
# line_edit = QLineEdit()
# layout.addWidget(line_edit)
#
# # Create a QPushButton object with a caption on it
# qbtn = QPushButton('Add Label')
#
# # Add the QPushButton to the layout
# layout.addWidget(qbtn)
#
# # Close the application whent the button is pressed
# # Here I am using slots & signals, which I will demonstrate later in this tutorial.
# qbtn.clicked.connect(lambda: addLabel(layout, line_edit.text()))
#
#
# # Show the parent Widget
# window.show()
#
# # Run the main Qt loop
# sys.exit(app.exec())

# ------------------------------------------

# Labels

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
# from PyQt6.QtCore import Qt
#
# # Create the Qt Application
# app = QApplication(sys.argv)
#
# # Create the parent widget and the QVBoxLayout Layout Manager
# window = QWidget()
# layout = QVBoxLayout(window)
#
# # Create a Label beforehand
# firstLabel = QLabel('Countrycode: BE')
# secondLabel = QLabel('Brussels waffles are the best food ever.')
#
# # Add Labels to layout, creating an anonymous label while adding
# layout.addWidget(firstLabel)
# layout.addWidget(secondLabel, alignment=Qt.AlignmentFlag.AlignJustify)
# layout.addWidget(QLabel('The Belgian flag consists of the colors black, yellow and red', wordWrap=True), alignment=Qt.AlignmentFlag.AlignLeft)
#
# # using setText() we can change the caption of a label
# firstLabel.setText('Belgium is a country located in Europe')
# firstLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
#
# # Show the parent Widget
# window.show()
#
# # Run the main Qt Loop
# sys.exit(app.exec())


# from PyQt6.QtCore import pyqtSlot
#
# # Slot function - Note the @pyqtSlot() annotation!
# @pyqtSlot()
# def hello_world():
#   print('Button is clicked, Hello World!')

# ------------------------------------------

# Signal and Slots

# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton
# from PyQt6.QtCore import pyqtSlot
#
#
# @pyqtSlot()
# def hello_world():
#     print('You shall not pass')
#
#
# # Create the Qt Application
# app = QApplication(sys.argv)
#
# # Create a QPushButton Object
# button = QPushButton('Click me')
#
# # Connect the button to the hello_world slot function
# button.clicked.connect(hello_world)
#
# # Show the button to the user
# button.show()
#
# # Run the main Qt loop
# sys.exit(app.exec())

# ------------------------------------------

# Buttons
