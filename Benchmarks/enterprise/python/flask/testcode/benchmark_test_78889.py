# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest78889():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
