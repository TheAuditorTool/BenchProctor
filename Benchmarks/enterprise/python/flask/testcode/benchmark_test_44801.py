# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest44801():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    pending = list(str(config_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
