# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest71517():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    requests.get(str(data))
    return jsonify({"result": "success"})
