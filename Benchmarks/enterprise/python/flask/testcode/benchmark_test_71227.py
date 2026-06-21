# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def BenchmarkTest71227():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    session['data'] = str(data)
    return jsonify({"result": "success"})
