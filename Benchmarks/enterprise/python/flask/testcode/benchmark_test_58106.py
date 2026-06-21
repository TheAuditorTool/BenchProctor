# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest58106():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
