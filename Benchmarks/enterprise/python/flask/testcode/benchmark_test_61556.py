# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest61556():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
