# SPDX-License-Identifier: Apache-2.0
import logging
import re
from dataclasses import dataclass
from flask import jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest09619():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
