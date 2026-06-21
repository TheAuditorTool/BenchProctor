# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest02064():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
