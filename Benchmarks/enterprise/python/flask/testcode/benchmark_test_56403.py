# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re


def BenchmarkTest56403(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
