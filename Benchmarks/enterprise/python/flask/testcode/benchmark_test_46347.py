# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest46347():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
