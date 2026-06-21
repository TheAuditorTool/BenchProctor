# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest33101():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
