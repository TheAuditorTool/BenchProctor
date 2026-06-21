# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest46572():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
