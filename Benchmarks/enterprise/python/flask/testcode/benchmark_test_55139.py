# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest55139():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
