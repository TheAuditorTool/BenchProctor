# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest15579():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
