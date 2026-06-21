# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest79955():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data, _sep, _rest = str(prop_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
