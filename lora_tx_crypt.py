# LoRa TX with Encryption

import time
from cryptolib import aes
import os

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

def pad(data: bytes) -> bytes:
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len

def encrypt(message: bytes) -> bytes:
    iv = os.urandom(16)  # Generate random IV
    cipher = aes(CRYPT_KEY, 2, iv)
    return iv + cipher.encrypt(pad(message))  # packet = iv + ciphertext

def update_display(counter):
    display.fill(0)
    display.text("Sending...", 0, 0, 1)
    display.text(str(counter), 0, 12, 1)
    if KEY_INSECURE:
        display.text("Warning: Insecure Key!", 0, 24, 1)
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
        modem.send(encrypt(f"Hello world from MicroPython #{counter}".encode()))
        time.sleep(2)
        counter += 1

main()