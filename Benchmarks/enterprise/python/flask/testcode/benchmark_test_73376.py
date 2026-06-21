# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest73376():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = to_text(query_array)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
