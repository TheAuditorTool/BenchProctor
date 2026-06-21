# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest50698(path_param):
    path_value = path_param
    data = relay_value(path_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
