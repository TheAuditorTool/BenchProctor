# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
import json
from flask import jsonify


def BenchmarkTest21136():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = json.loads(file_value).get('value', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
