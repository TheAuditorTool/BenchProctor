# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest24152():
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    json.loads(data)
    return jsonify({"result": "success"})
