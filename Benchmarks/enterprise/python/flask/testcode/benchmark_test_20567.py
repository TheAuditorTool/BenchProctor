# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
import importlib


def BenchmarkTest20567():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
