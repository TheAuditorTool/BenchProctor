# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest58181():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    request_state['last_input'] = config_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
