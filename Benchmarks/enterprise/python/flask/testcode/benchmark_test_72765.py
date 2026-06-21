# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest72765():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
