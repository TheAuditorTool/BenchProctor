# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest23764():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
