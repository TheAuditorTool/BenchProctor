# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest41954():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
