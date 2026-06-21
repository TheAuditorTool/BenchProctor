# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import ast


def BenchmarkTest25453():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
