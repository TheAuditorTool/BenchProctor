# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest71017():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
