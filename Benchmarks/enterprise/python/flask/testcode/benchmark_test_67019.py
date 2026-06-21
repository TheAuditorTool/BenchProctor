# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest67019(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
