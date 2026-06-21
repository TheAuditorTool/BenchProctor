# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest26727():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ns = SimpleNamespace(payload=prop_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
