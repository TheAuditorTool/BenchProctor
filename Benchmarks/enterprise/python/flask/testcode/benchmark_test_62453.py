# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62453():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
