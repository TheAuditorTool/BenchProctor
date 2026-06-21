# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest46008():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
