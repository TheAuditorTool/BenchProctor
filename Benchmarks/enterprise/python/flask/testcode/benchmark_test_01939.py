# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify


def BenchmarkTest01939():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
