# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest08270():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    kind = 'json' if str(query_array).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = query_array
            data = parsed
        case _:
            data = query_array
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
