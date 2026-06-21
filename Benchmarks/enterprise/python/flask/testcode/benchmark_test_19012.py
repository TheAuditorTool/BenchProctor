# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest19012():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
