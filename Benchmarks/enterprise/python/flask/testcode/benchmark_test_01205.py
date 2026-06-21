# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest01205():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    json.loads(data)
    return jsonify({"result": "success"})
