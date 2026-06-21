# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest18459():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    logging.info('User action: ' + str(yaml_value))
    return jsonify({"result": "success"})
