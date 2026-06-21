# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import request, jsonify
import os


def BenchmarkTest49349():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
