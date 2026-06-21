# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest79122():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
