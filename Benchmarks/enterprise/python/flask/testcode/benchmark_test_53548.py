# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import json


def BenchmarkTest53548():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = json.loads(yaml_value).get('value', yaml_value)
    except (json.JSONDecodeError, AttributeError):
        data = yaml_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
