# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest74783():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    session.clear()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
