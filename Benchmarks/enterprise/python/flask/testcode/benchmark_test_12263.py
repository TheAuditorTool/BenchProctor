# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest12263():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = default_blank(dotenv_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
