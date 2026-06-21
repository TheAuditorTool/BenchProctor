# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
import subprocess


def BenchmarkTest74884():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
