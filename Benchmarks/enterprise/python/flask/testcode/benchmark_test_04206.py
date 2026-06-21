# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest04206():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        result = int(str(env_value))
    except Exception:
        pass
    return jsonify({"result": "success"})
