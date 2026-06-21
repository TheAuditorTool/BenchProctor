# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest38012():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
