# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest57957():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = '%s' % (yaml_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
