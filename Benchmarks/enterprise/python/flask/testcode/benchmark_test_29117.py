# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest29117():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
