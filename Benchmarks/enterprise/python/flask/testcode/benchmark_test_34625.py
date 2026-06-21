# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest34625():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(yaml_value)
    data = collected
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
