# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def BenchmarkTest37475():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    session['data'] = str(data)
    return jsonify({"result": "success"})
