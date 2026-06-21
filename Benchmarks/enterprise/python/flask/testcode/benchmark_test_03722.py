# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest03722():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = str(prop_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
