# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest43016():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = config_value if config_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
