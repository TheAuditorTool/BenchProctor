# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest40317():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
