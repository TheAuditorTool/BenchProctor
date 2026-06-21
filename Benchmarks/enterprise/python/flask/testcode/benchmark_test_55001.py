# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest55001():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
