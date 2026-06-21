# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest06431():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
