# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest27391():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
