# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest74369():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
