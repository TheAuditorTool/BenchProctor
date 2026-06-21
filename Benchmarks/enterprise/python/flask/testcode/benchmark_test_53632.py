# SPDX-License-Identifier: Apache-2.0
import jwt
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest53632():
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
