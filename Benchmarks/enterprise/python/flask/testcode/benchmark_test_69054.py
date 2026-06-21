# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest69054():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
