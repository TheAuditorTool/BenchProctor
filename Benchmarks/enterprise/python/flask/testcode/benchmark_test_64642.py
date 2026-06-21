# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest64642():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(yaml_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
