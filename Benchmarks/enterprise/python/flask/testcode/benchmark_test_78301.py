# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest78301():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
