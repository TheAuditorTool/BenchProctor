# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest29605():
    auth_header = request.headers.get('Authorization', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(auth_header).encode())
    return jsonify({'length': len(ciphertext)}), 200
