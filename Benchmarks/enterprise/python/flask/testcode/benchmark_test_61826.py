# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest61826():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
