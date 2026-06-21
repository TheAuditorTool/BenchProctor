# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05407():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
