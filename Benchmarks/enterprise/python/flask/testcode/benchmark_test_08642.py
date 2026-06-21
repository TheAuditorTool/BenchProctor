# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08642():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
