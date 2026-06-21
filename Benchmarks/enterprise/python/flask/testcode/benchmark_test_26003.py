# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import ast


def BenchmarkTest26003():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = str(ast.literal_eval(yaml_value))
    except (ValueError, SyntaxError):
        data = yaml_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
