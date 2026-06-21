# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest13039():
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
