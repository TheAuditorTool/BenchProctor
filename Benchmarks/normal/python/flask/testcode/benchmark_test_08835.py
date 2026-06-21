# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest08835():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
