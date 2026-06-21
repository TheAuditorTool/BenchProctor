# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest05593():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
