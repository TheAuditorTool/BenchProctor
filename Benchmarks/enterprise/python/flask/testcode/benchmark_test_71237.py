# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest71237():
    origin_value = request.headers.get('Origin', '')
    requests.post('https://api.prod.internal/data', data=str(origin_value), verify=True)
    return jsonify({"result": "success"})
