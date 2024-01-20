import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QLabel, QLineEdit, QVBoxLayout, QHBoxLayout,
    QMainWindow, QApplication, QWidget, QPushButton,
    QGraphicsView, QGraphicsScene
)
from PyQt5.QtGui import QImage, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from random import randint

from Pattern import Pattern

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Double Slit Interference Simulation")

        master_layout = QVBoxLayout()
        toolbar = QHBoxLayout()
        Work_Layout = QHBoxLayout()
        Para = QVBoxLayout()

        master_layout.setContentsMargins(0, 0, 0, 0)
        master_layout.setSpacing(20)

        # Setup toolbar
        toolbar.addWidget(QLabel('Toolbar'))

        # Setup Parameter Control
        label_names = ["Amplitude", "Wavelength", "Width of Slit", "Separation", "Distance to Screen", "Screen resolution", "Noise", "Random noise", "Random Seed"]

        self.Parameter = {}
        for label_name in label_names:
            label = QLabel(label_name)
            self.Parameter[label_name] = QLineEdit()

            # Add the label and input box to the layout
            Para.addWidget(label)
            Para.addWidget(line_edit)
        simulate_button = QPushButton("Simulate")
        simulate_button.clicked.connect(self.plotGraphMatplotlib)  # Connect the button click to the plotGraphMatplotlib method
        Para.addWidget(simulate_button)

        # Setup Matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Setup WorkArea
        Work_Layout.addLayout(Para)
        Work_Layout.addWidget(self.canvas)  # Add Matplotlib canvas to the layout

        # Setup the master area.
        master_layout.addLayout(toolbar)
        master_layout.addLayout(Work_Layout)

        widget = QWidget()
        widget.setLayout(master_layout)
        self.setCentralWidget(widget)

    def plotGraphMatplotlib(self):
        pattern = Pattern()
        image_data = pattern.GenerateWave(self.Parameter['Amplitude'],self.Parameter['Wavelength'],self.Parameter["Width of Slit"],self.Parameter["Separation"],self.Parameter["Distance to Screen"],self.Parameter["Screen resolution"],self.Parameter["Noise"],self.Parameter["Random noise"],self.Parameter["Random Seed"])

        # Plot the image using Matplotlib
        self.ax.imshow(image_data, cmap='gray')
        self.canvas.draw()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
