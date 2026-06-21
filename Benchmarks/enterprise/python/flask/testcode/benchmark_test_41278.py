# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest41278():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
