# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def BenchmarkTest10337():
    env_value = os.environ.get('USER_INPUT', '')
    processed = shlex.quote(env_value)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
