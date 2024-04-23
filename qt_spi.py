import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import spidev

class SpiControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('SPI Control App')

        self.turnOnButton = QPushButton('Turn On', self)
        self.turnOnButton.clicked.connect(self.turnOn)

        self.turnOffButton = QPushButton('Turn Off', self)
        self.turnOffButton.clicked.connect(self.turnOff)
        self.turnOffButton.move(0, 50)

    def turnOn(self):
        spi = spidev.SpiDev()
        spi.open(2, 0)  # Assuming SPI bus 2, device 0
        spi.mode = 0b00
        spi.lsbfirst = False
        spi.max_speed_hz = 1000
        data = 0x01  # Send 1 to turn on
        spi.xfer([data])  # Pass data as a list
        spi.close()

    def turnOff(self):
        spi = spidev.SpiDev()
        spi.open(2, 0)  # Assuming SPI bus 2, device 0
        spi.mode = 0b00
        spi.lsbfirst = False
        spi.max_speed_hz = 1000
        data = 0x00  # Send 0 to turn off
        spi.xfer([data])  # Pass data as a list
        spi.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpiControlApp()
    ex.show()
    sys.exit(app.exec_()
