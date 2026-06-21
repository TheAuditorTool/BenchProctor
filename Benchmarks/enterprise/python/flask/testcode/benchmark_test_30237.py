# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def BenchmarkTest30237():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(prop_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
