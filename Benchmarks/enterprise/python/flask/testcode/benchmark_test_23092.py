# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest23092(path_param):
    path_value = path_param
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(path_value)
    return jsonify({"result": "success"})
