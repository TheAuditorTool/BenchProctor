# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def BenchmarkTest32148():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
