# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest23109():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    request_state['last_input'] = prop_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
