# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest69171():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
