# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest72170():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
