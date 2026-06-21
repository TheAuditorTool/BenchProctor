# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest73450():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
