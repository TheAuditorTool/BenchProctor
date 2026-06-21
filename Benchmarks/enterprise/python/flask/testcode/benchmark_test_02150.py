# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest02150():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    if prop_value:
        data = prop_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
