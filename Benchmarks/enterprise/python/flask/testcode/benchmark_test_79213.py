# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest79213():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
