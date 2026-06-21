# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest22123():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
