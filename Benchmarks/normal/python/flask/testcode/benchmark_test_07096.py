# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest07096():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
