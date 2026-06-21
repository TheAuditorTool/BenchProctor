# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os
import ast


def BenchmarkTest71221():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
