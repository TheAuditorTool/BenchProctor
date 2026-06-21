# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast


def BenchmarkTest67510():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
