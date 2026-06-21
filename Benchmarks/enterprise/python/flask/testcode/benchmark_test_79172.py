# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest79172():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', forwarded_ip):
        return jsonify({'error': 'forbidden'}), 400
    processed = forwarded_ip
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
