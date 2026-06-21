# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest52843():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = '%s' % (prop_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
