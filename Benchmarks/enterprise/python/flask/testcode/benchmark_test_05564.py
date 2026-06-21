# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest05564():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
