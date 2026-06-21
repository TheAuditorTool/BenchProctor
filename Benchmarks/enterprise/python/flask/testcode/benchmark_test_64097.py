# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest64097():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
