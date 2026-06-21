# SPDX-License-Identifier: Apache-2.0
import logging
import re
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest07273():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = FormData(payload=config_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
