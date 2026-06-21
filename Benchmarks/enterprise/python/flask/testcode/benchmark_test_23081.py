# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest23081():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = default_blank(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return jsonify({"result": "success"})
