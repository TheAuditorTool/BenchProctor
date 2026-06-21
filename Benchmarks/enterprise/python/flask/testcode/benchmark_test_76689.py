# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76689():
    cookie_value = request.cookies.get('session_token', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(cookie_value))
    return jsonify({"result": "success"})
