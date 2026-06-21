# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest47417():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
