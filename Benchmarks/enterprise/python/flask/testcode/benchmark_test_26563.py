# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest26563():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
