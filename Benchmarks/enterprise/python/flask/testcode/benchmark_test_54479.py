# SPDX-License-Identifier: Apache-2.0
import logging
import json
from flask import jsonify


def BenchmarkTest54479():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = json.loads(yaml_value).get('value', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
