# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from flask import session
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest12212(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
