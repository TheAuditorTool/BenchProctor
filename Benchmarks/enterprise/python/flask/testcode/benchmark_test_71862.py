# SPDX-License-Identifier: Apache-2.0
import jwt
import keyring
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest71862():
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
