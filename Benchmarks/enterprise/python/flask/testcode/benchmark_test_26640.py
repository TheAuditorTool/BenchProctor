# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26640():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
