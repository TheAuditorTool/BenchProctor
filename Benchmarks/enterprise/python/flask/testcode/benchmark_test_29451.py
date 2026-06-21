# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest29451():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = ' '.join(str(prop_value).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
