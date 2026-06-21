# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest01059():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
