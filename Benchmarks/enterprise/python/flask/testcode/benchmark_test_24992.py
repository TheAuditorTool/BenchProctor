# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest24992():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    logging.info('User action: ' + str(prop_value))
    return jsonify({"result": "success"})
