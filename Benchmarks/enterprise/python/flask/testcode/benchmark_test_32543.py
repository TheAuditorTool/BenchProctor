# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest32543():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
