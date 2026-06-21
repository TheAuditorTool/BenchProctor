# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest47369():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    int(str(data))
    return jsonify({"result": "success"})
