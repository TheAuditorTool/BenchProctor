# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest70755():
    referer_value = request.headers.get('Referer', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(referer_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
