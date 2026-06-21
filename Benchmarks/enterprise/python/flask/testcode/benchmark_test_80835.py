# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


def BenchmarkTest80835():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
