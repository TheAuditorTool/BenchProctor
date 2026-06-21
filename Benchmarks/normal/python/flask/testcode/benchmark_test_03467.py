# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from flask import session
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest03467(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
