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
    display.text("Receiving...", 0, 0, 1)
    display.text(str(counter), 0, 12, 1)
    display.show()

def main():
    print("Initializing...")
    modem = get_modem(LORA_CFG)

    display.fill(0)
    display.text("Receiving...", 0, 0, 1)
    display.show()

    counter = 0
    rx_counter = 0
    while True:
        rx = modem.recv(timeout_ms=5000)

        if rx:
            print(f"Received: {rx}")
            rx_counter += 1
            update_display(rx_counter)
        else:
            print("RX Timeout!")
        time.sleep(1)
        counter += 1

main()