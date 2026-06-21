# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest31862():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
