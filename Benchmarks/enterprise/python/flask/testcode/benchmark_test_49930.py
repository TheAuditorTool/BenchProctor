# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest49930():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
