# LoRa RX with Encryption

import time
from cryptolib import aes

# Encryption/Decryption key
# REPLACE WITH YOUR OWN
CRYPT_KEY = b"OYc0MeKTjZS8vl2KNNEIIt6aWa8sVFfC"
# After replacing keys with your own, switch to False to disable the warning
KEY_INSECURE = True

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

def unpad(data):
    pad_size = data[-1]
    return data[:-pad_size]

def decrypt(packet: bytes) -> bytes:
    iv = packet[:16]  # first 16 bytes = iv
    data = packet[16:]  # rest is ciphertext
    cipher = aes(CRYPT_KEY, 2, iv)
    return unpad(cipher.decrypt(data))

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
            print("Received: ", rx)
            print(f"Received (after decryption): {decrypt(rx)}")
            rx_counter += 1
            update_display(rx_counter)
        else:
            print("RX Timeout!")
        time.sleep(1)
        counter += 1

main()