# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest05162():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
