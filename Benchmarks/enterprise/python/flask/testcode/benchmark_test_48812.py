# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest48812():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
