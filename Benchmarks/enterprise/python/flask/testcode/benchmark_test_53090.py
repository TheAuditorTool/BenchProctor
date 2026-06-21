# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def BenchmarkTest53090():
    env_value = os.environ.get('USER_INPUT', '')
    session['user'] = str(env_value)
    return jsonify({"result": "success"})
