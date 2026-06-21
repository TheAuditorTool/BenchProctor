# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest56646():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
