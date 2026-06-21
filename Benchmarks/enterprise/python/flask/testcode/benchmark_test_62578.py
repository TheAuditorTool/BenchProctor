# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re


def BenchmarkTest62578(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
