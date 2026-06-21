# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest50191(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
