# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import tempfile


@dataclass
class FormData:
    payload: str

def BenchmarkTest61337():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
