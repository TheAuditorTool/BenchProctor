# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest23985():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    ns = SimpleNamespace(payload=file_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
