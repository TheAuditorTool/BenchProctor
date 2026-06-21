# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest48326():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
