# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify


def BenchmarkTest02479():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
