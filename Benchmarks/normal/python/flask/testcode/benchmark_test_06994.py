# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest06994():
    multipart_value = request.form.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = multipart_value
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
