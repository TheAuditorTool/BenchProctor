# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify
import os


def BenchmarkTest19010():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    pending = list(str(dotenv_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
