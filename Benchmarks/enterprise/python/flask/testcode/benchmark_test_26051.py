# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest26051():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
