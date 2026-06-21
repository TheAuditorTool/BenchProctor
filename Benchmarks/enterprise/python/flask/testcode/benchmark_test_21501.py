# SPDX-License-Identifier: Apache-2.0
import logging
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest21501():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
