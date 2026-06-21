# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


def BenchmarkTest15956():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
