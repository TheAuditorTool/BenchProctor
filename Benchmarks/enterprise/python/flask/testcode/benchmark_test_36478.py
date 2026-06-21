# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest36478(path_param):
    path_value = path_param
    data = unquote(path_value)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
