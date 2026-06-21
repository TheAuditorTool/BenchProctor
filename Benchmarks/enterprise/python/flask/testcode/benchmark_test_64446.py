# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest64446():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
