# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest74096():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
