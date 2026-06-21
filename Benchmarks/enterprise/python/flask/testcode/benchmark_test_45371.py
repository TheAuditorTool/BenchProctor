# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import ast


def BenchmarkTest45371():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = str(ast.literal_eval(prop_value))
    except (ValueError, SyntaxError):
        data = prop_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
