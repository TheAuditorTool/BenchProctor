# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest29595():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
