# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest22466(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
