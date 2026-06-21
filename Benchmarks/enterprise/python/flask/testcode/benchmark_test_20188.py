# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
import os
from flask import jsonify


def BenchmarkTest20188():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
