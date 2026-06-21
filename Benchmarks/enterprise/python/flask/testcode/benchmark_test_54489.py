# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest54489():
    env_value = os.environ.get('USER_INPUT', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(env_value) + ',data\n')
    return jsonify({"result": "success"})
