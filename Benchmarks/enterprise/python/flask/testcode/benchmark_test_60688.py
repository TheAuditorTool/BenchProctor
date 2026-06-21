# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest60688():
    env_value = os.environ.get('USER_INPUT', '')
    os.system('echo ' + str(env_value))
    return jsonify({"result": "success"})
