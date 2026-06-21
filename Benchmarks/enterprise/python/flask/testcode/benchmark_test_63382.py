# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def relay_value(value):
    return value

def BenchmarkTest63382():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
