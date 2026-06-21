# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest05767(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
