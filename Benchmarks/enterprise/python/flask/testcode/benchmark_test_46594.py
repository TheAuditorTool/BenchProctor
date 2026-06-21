# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest46594():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(query_array)):
        return jsonify({'error': 'invalid input'}), 400
    processed = query_array
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
