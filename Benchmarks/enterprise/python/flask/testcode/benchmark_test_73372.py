# SPDX-License-Identifier: Apache-2.0
import logging
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest73372():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
