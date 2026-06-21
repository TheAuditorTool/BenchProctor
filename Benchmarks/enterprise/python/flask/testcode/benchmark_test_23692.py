# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest23692():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data, _sep, _rest = str(yaml_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
