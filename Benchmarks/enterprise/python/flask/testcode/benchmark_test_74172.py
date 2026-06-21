# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest74172():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    eval(str(data))
    return jsonify({"result": "success"})
