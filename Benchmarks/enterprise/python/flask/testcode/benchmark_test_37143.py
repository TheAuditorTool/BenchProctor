# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest37143():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = str(yaml_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
