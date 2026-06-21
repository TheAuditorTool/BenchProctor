# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def BenchmarkTest00435():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    session['user'] = str(data)
    return jsonify({"result": "success"})
