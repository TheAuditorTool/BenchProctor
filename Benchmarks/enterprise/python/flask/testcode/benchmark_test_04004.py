# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
import base64
from flask import request, jsonify


def BenchmarkTest04004():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
