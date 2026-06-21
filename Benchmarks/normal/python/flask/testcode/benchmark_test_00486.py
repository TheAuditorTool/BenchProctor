# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify


def BenchmarkTest00486():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
