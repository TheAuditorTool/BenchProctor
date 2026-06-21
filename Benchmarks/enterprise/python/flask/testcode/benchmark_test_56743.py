# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest56743():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
