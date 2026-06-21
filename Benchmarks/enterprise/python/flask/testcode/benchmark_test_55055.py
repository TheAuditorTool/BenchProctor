# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest55055():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
