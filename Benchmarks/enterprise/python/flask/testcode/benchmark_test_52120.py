# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest52120():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
