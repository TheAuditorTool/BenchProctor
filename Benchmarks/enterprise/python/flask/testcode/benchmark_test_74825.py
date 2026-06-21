# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest74825():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    if yaml_value:
        data = yaml_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
