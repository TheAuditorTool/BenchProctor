# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest71444():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
