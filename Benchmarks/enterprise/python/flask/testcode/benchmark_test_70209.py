# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest70209(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
