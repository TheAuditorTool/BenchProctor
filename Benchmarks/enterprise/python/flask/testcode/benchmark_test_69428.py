# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest69428():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
