# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14579():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    reader = make_reader(yaml_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
