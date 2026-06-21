# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest26040():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
