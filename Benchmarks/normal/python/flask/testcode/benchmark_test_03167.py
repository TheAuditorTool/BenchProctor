# SPDX-License-Identifier: Apache-2.0
import logging
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest03167():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
