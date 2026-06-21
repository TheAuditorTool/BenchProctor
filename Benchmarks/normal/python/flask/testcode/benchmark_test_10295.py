# SPDX-License-Identifier: Apache-2.0
import logging
import re
import os
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest10295():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
