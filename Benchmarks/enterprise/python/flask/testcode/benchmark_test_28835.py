# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest28835():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
