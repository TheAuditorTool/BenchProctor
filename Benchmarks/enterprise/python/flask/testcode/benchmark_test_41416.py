# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest41416():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    prefix = ''
    data = prefix + str(config_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
