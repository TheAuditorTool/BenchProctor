# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest12983():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
