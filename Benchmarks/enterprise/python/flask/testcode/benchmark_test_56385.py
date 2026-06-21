# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest56385():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data, _sep, _rest = str(config_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
