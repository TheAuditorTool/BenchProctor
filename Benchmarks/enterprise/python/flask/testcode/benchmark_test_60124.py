# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest60124():
    ua_value = request.headers.get('User-Agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(ua_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = ua_value
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
