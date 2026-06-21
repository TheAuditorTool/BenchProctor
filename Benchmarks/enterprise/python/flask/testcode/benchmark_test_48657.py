# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def BenchmarkTest48657():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(config_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
