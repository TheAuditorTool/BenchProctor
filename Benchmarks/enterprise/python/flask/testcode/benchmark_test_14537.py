# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14537():
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
