# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest34406():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    int(str(data))
    return jsonify({"result": "success"})
