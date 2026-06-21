# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest58757():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    int(str(data))
    return jsonify({"result": "success"})
