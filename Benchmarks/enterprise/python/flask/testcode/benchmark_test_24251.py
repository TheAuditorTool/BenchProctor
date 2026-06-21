# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest24251():
    origin_value = request.headers.get('Origin', '')
    data = default_blank(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return jsonify({"result": "success"})
