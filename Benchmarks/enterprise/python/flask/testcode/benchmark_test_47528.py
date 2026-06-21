# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest47528():
    secret_value = 'default_config_label'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
