# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest40739(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
