# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest04900():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
