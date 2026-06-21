# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest53751():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    os.remove(str(data))
    return jsonify({"result": "success"})
