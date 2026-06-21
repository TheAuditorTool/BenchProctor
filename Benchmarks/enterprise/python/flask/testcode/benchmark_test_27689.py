# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest27689():
    env_value = os.environ.get('USER_INPUT', '')
    subprocess.run([str(env_value), '--status'], shell=False)
    return jsonify({"result": "success"})
