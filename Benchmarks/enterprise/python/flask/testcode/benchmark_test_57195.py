# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def ensure_str(value):
    return str(value)

def BenchmarkTest57195():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ensure_str(forwarded_ip)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
