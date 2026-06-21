# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest56274():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
