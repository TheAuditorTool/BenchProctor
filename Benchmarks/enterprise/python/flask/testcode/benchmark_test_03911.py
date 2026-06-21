# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03911():
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
