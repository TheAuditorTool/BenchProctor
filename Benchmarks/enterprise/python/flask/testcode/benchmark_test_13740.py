# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest13740():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
