# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify
import json


def BenchmarkTest22333():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    try:
        data = json.loads(query_array).get('value', query_array)
    except (json.JSONDecodeError, AttributeError):
        data = query_array
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
