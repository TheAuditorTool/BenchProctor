# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest29351():
    env_value = os.environ.get('USER_INPUT', '')
    with open('/var/uploads/' + str(env_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
