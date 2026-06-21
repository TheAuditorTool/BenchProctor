# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest06115():
    origin_value = request.headers.get('Origin', '')
    requests.post('http://api.prod.internal/data', data=str(origin_value))
    return jsonify({"result": "success"})
