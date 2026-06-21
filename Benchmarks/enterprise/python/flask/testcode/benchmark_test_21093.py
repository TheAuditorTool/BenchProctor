# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21093():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
