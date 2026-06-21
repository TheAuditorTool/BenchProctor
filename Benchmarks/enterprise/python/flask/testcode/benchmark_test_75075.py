# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest75075():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
