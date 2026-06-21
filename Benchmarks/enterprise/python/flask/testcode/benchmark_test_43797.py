# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest43797():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = yaml_value if yaml_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
