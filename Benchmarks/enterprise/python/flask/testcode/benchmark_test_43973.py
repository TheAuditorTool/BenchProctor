# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest43973(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
