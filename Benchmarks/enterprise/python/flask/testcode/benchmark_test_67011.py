# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify
import json


def BenchmarkTest67011():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
