# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest01559():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    json.loads(data)
    return jsonify({"result": "success"})
