# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest14080():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = '%s' % str(yaml_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
