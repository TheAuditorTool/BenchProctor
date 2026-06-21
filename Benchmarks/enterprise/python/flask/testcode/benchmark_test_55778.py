# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest55778():
    xml_value = request.get_data(as_text=True)
    data = to_text(xml_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
