# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest67831():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = (lambda v: v.strip())(prop_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
