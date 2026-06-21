# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest56814():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
