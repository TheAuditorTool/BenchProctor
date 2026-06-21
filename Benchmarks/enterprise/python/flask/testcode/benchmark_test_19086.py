# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest19086():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = f'{yaml_value:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
