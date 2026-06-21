# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def BenchmarkTest00889():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(yaml_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
