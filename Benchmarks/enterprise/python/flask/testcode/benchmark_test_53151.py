# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta
import ast


def BenchmarkTest53151():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
