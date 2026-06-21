# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def BenchmarkTest32664():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
