# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest30850():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
