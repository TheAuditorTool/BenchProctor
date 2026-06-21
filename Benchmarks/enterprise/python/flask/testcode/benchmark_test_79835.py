# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79835():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
