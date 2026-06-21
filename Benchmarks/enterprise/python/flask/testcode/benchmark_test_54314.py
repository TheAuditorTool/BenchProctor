# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest54314():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    json.loads(data)
    return jsonify({"result": "success"})
