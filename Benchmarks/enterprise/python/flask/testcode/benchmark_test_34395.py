# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34395():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
