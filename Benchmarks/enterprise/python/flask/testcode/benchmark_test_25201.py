# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest25201():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
