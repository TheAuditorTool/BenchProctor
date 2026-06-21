# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
import ast


def BenchmarkTest43490():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
