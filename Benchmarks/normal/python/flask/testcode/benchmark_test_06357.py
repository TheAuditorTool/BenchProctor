# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify
import time


def BenchmarkTest06357():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
