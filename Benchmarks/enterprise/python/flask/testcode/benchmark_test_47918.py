# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest47918():
    xml_value = request.get_data(as_text=True)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(xml_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
