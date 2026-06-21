# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest66392():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
