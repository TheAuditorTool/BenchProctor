# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest80361():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
