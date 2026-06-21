# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def BenchmarkTest43470():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    parts = []
    for token in str(config_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
