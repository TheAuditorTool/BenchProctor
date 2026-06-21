# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest31912():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
