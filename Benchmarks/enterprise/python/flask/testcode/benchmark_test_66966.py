# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest66966():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    json.loads(data)
    return jsonify({"result": "success"})
