# SPDX-License-Identifier: Apache-2.0
import json
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest33596():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    json.loads(data)
    return jsonify({"result": "success"})
