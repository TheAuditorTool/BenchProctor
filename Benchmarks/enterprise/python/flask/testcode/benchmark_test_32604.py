# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest32604():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
