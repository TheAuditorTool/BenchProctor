# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest09476():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
