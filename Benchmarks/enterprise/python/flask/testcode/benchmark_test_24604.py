# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest24604():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    requests.get(str(data))
    return jsonify({"result": "success"})
