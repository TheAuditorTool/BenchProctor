# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest16500():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
