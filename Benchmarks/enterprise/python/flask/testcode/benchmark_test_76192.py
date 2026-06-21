# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify


def BenchmarkTest76192():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
