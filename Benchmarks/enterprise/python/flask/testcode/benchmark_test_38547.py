# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest38547():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    session.clear()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
