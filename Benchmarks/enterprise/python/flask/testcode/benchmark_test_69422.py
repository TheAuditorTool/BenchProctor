# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import request, jsonify


def BenchmarkTest69422():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
