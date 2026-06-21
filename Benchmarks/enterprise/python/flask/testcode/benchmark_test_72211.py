# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72211():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
