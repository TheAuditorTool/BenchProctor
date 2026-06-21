# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest29425():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
