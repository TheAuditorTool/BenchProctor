# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def BenchmarkTest36196():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    session['data'] = str(data)
    return jsonify({"result": "success"})
