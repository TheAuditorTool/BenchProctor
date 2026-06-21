# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest05998():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(json_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
