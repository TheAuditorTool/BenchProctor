# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import re


def BenchmarkTest52899(path_param):
    path_value = path_param
    data = unquote(path_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
