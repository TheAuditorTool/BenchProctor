# SPDX-License-Identifier: Apache-2.0
import requests
import base64
from flask import request, jsonify


def BenchmarkTest74846():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
