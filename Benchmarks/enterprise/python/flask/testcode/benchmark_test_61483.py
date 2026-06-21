# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest61483():
    raw_body = request.get_data(as_text=True)
    requests.post('http://api.prod.internal/data', data=str(raw_body))
    return jsonify({"result": "success"})
