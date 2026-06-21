# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest49481():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    eval(str(data))
    return jsonify({"result": "success"})
