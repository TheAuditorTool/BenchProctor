# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os
from flask import jsonify
import time
import ast


def BenchmarkTest24833():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
