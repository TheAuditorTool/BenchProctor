# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify
from flask import current_app
import json
from datetime import timedelta


def BenchmarkTest71219():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
