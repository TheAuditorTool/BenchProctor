# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79019():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
