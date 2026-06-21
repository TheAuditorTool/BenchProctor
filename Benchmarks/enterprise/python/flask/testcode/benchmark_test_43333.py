# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest43333():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
