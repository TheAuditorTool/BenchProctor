# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest19116():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % str(config_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
