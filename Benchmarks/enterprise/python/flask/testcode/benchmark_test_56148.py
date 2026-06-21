# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest56148():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
