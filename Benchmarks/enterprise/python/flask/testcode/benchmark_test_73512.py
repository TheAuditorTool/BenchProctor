# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest73512(path_param):
    path_value = path_param
    data = f'{path_value}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
