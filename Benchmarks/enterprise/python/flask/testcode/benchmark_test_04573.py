# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest04573():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
