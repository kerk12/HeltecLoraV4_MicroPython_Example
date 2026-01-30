from machine import Pin, I2C
import ssd1306, time
from lora import SX1262
from machine import SPI
import builtins
# See datasheet: https://resource.heltec.cn/download/WiFi_LoRa_32_V4/datasheet/WiFi_LoRa_32_V4.2.0.pdf

# Power on Vext. Needed for OLED to work
vext = Pin(36, Pin.OUT)
vext.value(0)  # active low

# # Reset OLED
_oled_rst = Pin(21, Pin.OUT)
_oled_rst.value(0)
time.sleep_ms(10)
_oled_rst.value(1)
time.sleep_ms(20)

oled_i2c = I2C(1, sda=Pin(17), scl=Pin(18), freq=400000)
print("Display detected on: ", oled_i2c.scan())  # should show [60]
display = ssd1306.SSD1306_I2C(128, 64, oled_i2c, addr=0x3C)

print("Use `display` to access display.")

def get_modem(cfg):
    """
    Used to get the modem when doing RX/TX
    @param cfg: The LoRa Config
    """

    # Heltec V4 SX1262 SPI pins
    # See datasheet: https://resource.heltec.cn/download/WiFi_LoRa_32_V4/datasheet/WiFi_LoRa_32_V4.2.0.pdf
    spi = SPI(
        1,
        baudrate=2_000_000,
        polarity=0,
        phase=0,
        sck=Pin(9),
        mosi=Pin(10),
        miso=Pin(11),
    )

    # Chip Select, also known as NSS
    cs = Pin(8, Pin.OUT)

    modem = SX1262(
        spi, cs,
        busy=Pin(13, Pin.IN),     # Required on SX126x
        dio1=Pin(14, Pin.IN),     # Recommended
        reset=Pin(12, Pin.OUT),   # Recommended
        lora_cfg=cfg,
        dio3_tcxo_millivolts=1800,  # https://github.com/micropython/micropython-lib/issues/870
    )
    return modem

builtins.get_modem = get_modem

import esp
esp.osdebug(None)
# import webrepl
# webrepl.start()