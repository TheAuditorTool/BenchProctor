# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest66836():
    user_id = request.args.get('id', '')
    data = to_text(user_id)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
