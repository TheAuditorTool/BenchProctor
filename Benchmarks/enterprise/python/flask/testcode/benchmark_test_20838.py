# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify


def BenchmarkTest20838():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
