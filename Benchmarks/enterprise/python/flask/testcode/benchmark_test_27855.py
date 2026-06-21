# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest27855():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
