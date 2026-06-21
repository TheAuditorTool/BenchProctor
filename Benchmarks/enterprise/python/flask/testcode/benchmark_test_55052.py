# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest55052():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
