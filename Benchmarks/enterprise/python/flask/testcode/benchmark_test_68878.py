# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest68878():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    eval(str(data))
    return jsonify({"result": "success"})
