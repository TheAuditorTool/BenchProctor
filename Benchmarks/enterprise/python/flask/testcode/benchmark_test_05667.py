# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
from flask import session
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest05667():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
