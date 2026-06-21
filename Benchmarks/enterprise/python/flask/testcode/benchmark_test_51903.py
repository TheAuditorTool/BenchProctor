# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest51903():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = prop_value if prop_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
