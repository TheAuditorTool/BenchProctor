# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest08334():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    json.loads(data)
    return jsonify({"result": "success"})
