# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest05617():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
