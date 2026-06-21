# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest05815():
    header_value = request.headers.get('X-Custom-Header', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(header_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
