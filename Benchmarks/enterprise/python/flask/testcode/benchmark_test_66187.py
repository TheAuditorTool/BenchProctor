# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest66187():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    exec(str(data))
    return jsonify({"result": "success"})
