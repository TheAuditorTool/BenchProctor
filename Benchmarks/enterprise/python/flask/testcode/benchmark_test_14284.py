# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest14284():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
