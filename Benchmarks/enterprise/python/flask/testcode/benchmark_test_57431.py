# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest57431(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
