# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest16350():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
