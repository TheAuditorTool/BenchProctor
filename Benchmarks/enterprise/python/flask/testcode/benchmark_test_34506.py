# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest34506():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
