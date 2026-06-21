# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest29231():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = ' '.join(str(config_value).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
