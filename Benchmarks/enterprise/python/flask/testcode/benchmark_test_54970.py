# SPDX-License-Identifier: Apache-2.0
from flask import session
import json
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest54970():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
