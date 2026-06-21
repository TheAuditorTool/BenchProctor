# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest30410():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
