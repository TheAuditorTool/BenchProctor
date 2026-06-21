# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest29246():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
