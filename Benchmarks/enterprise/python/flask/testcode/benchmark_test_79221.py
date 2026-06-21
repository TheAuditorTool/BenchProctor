# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest79221():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
