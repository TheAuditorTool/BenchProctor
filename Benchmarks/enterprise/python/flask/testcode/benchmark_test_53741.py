# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
import base64
from flask import jsonify


def BenchmarkTest53741():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = base64.b64decode(file_value).decode('utf-8', 'ignore')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
