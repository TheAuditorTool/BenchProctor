# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest02847():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return jsonify({"result": "success"})
