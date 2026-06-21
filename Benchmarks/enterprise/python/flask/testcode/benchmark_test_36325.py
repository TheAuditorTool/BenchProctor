# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest36325():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % (config_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
