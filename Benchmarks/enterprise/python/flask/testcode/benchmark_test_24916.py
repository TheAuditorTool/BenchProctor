# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest24916():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
