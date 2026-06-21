# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest79239():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    parts = str(yaml_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
