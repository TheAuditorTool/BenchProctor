# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest60965():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
