# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def BenchmarkTest70801(path_param):
    path_value = path_param
    if path_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
