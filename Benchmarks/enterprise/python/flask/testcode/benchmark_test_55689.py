# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest55689():
    referer_value = request.headers.get('Referer', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(referer_value).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return jsonify({"result": "success"})
