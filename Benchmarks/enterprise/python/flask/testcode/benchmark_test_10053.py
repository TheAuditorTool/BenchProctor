# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify
import time


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest10053():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
