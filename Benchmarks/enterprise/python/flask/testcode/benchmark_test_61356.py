# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest61356():
    header_value = request.headers.get('X-Custom-Header', '')
    data = normalise_input(header_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
