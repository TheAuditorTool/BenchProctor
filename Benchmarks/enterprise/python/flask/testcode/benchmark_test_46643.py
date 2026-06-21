# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest46643():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
