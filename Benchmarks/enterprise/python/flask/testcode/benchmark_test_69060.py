# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest69060():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = normalise_input(json_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
