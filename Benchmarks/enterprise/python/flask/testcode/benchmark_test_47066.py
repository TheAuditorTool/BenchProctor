# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def BenchmarkTest47066():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    session['data'] = str(data)
    return jsonify({"result": "success"})
