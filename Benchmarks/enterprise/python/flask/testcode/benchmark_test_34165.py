# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify


def BenchmarkTest34165():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
