# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest03472():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    requests.get(str(data))
    return jsonify({"result": "success"})
