# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest52477():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
