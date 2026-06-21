# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54428():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
