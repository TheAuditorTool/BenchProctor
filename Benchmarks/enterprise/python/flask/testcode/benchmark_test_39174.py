# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest39174():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
