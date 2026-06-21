# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09448():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
