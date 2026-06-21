# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import ast


def BenchmarkTest20387(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
