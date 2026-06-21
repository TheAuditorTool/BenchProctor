# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest41778():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
