# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest05933():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
