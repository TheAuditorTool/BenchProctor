# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13187():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
