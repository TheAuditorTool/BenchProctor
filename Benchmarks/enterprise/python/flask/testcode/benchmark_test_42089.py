# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest42089():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
