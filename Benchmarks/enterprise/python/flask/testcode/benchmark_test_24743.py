# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24743():
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
