# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest62813():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
