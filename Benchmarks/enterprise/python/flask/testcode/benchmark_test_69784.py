# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import ast


def BenchmarkTest69784():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
