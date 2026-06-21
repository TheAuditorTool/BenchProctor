# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest25474():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    eval(str(data))
    return jsonify({"result": "success"})
