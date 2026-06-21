# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest18569():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
