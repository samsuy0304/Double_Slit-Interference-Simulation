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
        label_names = ["Amplitude", "Wavelength", "Width of Slit", "Separation", "Distance to Screen", "Screen Width","Screen resolution", "Noise", "Random noise", "Random Seed"]
        defaults = [1.0, 1.0, 0.1, 0.5, 1.0, 1, 1000, 1, 0.1, 5555]
        self.Parameter = {}
        for label_name, default_value in zip(label_names, defaults):
            label = QLabel(label_name)
            self.Parameter[label_name] = QLineEdit()
            self.Parameter[label_name].setText(str(default_value))

            # Add the label and input box to the layout
            Para.addWidget(label)
            Para.addWidget(self.Parameter[label_name])

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
        
        amplitude = float(self.Parameter["Amplitude"].text())
        wavelength = float(self.Parameter["Wavelength"].text())
        width_of_slit = float(self.Parameter["Width of Slit"].text())
        separation = float(self.Parameter["Separation"].text())
        distance_to_screen = float(self.Parameter["Distance to Screen"].text())
        screen_width = int(self.Parameter["Screen Width"].text())
        screen_resolution = float(self.Parameter["Screen resolution"].text())
        noise = float(self.Parameter["Noise"].text())
        random_noise = float(self.Parameter["Random noise"].text())
        random_seed = float(self.Parameter["Random Seed"].text())
        pattern = Pattern(amplitude, wavelength, width_of_slit, separation, distance_to_screen, screen_width, screen_resolution, noise, random_noise, random_seed)
        # Retrieve values from QLineEdit, convert to float, and perform actions
        image_data = pattern.GenerateWave()#self.Parameter['Amplitude'],self.Parameter['Wavelength'],self.Parameter["Width of Slit"],self.Parameter["Separation"],self.Parameter["Distance to Screen"],self.Parameter["Screen resolution"],self.Parameter["Noise"],self.Parameter["Random noise"],self.Parameter["Random Seed"])

        # Plot the image using Matplotlib
        self.ax.imshow(image_data, cmap='gray')
        self.canvas.draw()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
