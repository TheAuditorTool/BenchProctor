# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest36622():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    prefix = ''
    data = prefix + str(prop_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
