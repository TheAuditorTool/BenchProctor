# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38687():
    cookie_value = request.cookies.get('session_token', '')
    raise RuntimeError('processing failed: ' + str(cookie_value))
    return jsonify({"result": "success"})
