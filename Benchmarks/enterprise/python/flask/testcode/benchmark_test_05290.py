# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re


def BenchmarkTest05290(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
