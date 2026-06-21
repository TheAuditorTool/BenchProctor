# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest44999():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
