import time

LORA_CFG = {
    "freq_khz": 915000,
    "sf": 7,
    "bw": 125,
    "coding_rate": 5,
    "preamble_len": 8,
    "output_power": 5,
    "crc": True,
    "invert_iq": False,
}

def update_display(counter):
    display.fill(0)
    display.text("Sending...", 0, 0, 1)
    display.text(str(counter), 0, 12, 1)
    display.show()

def main():
    print("Initializing...")
    modem = get_modem(LORA_CFG)

    display.fill(0)
    display.text("Sending...", 0, 0, 1)
    display.show()

    counter = 0
    while True:
        print("Sending...")
        update_display(counter)
        modem.send(f"Hello world from MicroPython #{counter}".encode())
        time.sleep(2)
        counter += 1

main()