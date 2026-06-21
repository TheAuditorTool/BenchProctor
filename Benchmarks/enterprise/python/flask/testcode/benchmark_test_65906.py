# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest65906():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
