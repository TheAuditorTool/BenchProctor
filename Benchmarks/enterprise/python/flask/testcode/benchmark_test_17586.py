# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest17586():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
