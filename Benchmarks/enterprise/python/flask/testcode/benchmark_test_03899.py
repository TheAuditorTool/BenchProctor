# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03899():
    host_value = request.headers.get('Host', '')
    data = default_blank(host_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
