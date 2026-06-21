# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest16473():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(dotenv_value).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return jsonify({"result": "success"})
