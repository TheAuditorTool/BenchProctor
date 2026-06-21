# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def ensure_str(value):
    return str(value)

def BenchmarkTest26547():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
