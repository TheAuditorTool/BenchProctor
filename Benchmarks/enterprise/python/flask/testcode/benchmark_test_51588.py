# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest51588():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
