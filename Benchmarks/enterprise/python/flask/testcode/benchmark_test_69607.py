# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69607():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    eval(str(data))
    return jsonify({"result": "success"})
