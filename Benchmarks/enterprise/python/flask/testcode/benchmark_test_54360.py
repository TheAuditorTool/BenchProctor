# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest54360():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(forwarded_ip).encode())
    return jsonify({'length': len(ciphertext)}), 200
