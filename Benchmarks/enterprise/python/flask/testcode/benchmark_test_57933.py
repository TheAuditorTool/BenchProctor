# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest57933():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
