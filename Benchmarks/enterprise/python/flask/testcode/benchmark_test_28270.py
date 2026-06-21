# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest28270():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
