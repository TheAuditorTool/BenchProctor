# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest43018():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    exec(str(data))
    return jsonify({"result": "success"})
