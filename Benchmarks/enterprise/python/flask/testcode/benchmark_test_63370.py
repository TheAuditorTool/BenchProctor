# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest63370():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = relay_value(prop_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
