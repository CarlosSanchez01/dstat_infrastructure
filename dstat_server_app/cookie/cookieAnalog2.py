import spidev

# first open up SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Initialize sensor

tempChannel = 0

def getReading(channel):
    # First pull the raw data from the chip
