# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify
import ast


def BenchmarkTest08405():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
