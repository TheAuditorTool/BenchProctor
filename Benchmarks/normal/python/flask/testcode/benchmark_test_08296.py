# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify
import time


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08296():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
