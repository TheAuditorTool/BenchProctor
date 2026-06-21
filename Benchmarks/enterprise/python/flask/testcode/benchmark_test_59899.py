# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59899():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
