# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest00211():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
