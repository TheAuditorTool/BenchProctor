# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


@dataclass
class FormData:
    payload: str

def BenchmarkTest26956():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
