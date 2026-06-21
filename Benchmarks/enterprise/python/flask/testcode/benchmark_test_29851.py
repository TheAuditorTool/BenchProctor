# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest29851():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
