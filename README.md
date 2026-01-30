# Heltec V4 MicroPython - Full Example

Coded by [Kyriakos Giannakis](https://www.linkedin.com/in/kgiannakis/) - [Flare](https://flare.gr)

## Intro:

I recently purchased a Heltec V4 board and wanted to flash MicroPython and see if I can get it working on a simple LoRa TX/RX.

In this repo, I'll be documenting the full way to get MicroPython working on this board and add various examples on the different functionalities.

## Step 1 - Get the tools

1. Install `esptool` and `mpremote`: `pip install -r requirements.txt`
2. Get yourself a copy of the latest MicroPython build for the ESP32 S3 (download the latest `.bin` file): [https://micropython.org/download/ESP32_GENERIC_S3/](https://micropython.org/download/ESP32_GENERIC_S3/)

## Step 2 - Flash micropython

1. Connect the heltec to your PC via usb and find the serial port it uses. This varies depending on the OS you're using.
2. Erase the flash: `esptool -p COM6 erase_flash`
3. Write the uPython bin: `esptool --baud 460800 write_flash 0 'D:\Downs\ESP32_GENERIC_S3-20251209-v1.27.0.bin'`
4. (Optional: do this if you've booted in flashing mode, to boot in normal mode) Unplug and replug the USB cable.
4. Connect mpremote to the device to verify everything's working: 
```bash
$ mpremote connect list
(You should see your device listed)
$ mpremote connect COM6 # (replace with your port)
(You should see a micropython REPL)
```
5. Congrats, you've successfully flashed micropython!

## Step 3 - Install required libraries

In order to get everything to work (the OLED display and the LoRa modem), you need to install some libraries from `micropython-lib`. Luckily, this is easily done
using `mpremote mip`:

```bash
$ mpremote mip install lora-sync lora-sx126x ssd1306
```

## Step 4 - Copy the example files

```bash
# Required: boot.py initializes your OLED display and adds a method to easily initialize your modem
$ mpremote fs cp ./boot.py :boot.py

# Now copy as needed. For example, if you want to test LoRa TX, copy lora_tx.py as main.py
$ mpremote fs cp ./lora_tx.py :main.py
# Alternatively, you can run the code using mpremote, without copying:
# $ mpremote run ./lora_tx.py
```

## Troubleshooting:

If you find that your controller is unresponsive and doesn't want to connect to serial and/or `mpremote`, you can try rebooting the controller in PRG mode:

1. Unplug the USB cable
2. Hold the PRG button
3. While holding, plug in the USB cable, keep holding PRG
4. Tap RST
5. Release PRG
6. The device should be in flashing mode. Go to Step 2.

## TODO:

- [X] TX Example
- [X] RX Example
- [ ] Encryption Example
- [ ] Deep Sleep

## Contributions:

Contributions are welcome to add/fix code. Hit me with your PRs!