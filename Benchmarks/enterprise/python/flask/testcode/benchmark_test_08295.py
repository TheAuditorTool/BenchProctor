# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from flask import current_app
from datetime import timedelta


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08295(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
