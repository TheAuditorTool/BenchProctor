# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest53859():
    raw_body = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
