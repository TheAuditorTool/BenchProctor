# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import ast


def BenchmarkTest46737():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
