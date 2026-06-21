# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest58686():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
