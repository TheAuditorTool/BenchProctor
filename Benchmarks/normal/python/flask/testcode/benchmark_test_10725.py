# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest10725():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
