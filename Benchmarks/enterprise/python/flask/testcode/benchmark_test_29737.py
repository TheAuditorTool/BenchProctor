# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest29737():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
