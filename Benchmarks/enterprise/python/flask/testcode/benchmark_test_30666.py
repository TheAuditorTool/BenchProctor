# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest30666(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
