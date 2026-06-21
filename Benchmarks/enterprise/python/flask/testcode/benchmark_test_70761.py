# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
import os
from flask import jsonify


def BenchmarkTest70761():
    env_value = os.environ.get('USER_INPUT', '')
    processed = shlex.quote(env_value)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
