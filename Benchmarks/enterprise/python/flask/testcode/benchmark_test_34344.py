# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest34344():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
