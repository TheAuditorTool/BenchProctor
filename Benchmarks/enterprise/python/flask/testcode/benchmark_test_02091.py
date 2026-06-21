# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest02091():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
