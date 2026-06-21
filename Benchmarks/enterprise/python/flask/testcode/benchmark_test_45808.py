# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify


def BenchmarkTest45808():
    env_value = os.environ.get('USER_INPUT', '')
    subprocess.run('echo ' + str(env_value), shell=True)
    return jsonify({"result": "success"})
