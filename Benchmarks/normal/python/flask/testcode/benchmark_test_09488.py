# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest09488(path_param):
    path_value = path_param
    data = to_text(path_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
