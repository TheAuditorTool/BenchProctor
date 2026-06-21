# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest35487():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
