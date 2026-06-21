# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest02990():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
