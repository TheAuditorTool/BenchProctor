# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import tempfile


@dataclass
class FormData:
    payload: str

def BenchmarkTest11355():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
