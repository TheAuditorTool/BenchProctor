# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest35328():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    logging.info('User action: ' + str(config_value))
    return jsonify({"result": "success"})
