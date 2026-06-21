# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re


def BenchmarkTest08276(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
