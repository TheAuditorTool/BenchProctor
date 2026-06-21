# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import importlib


def BenchmarkTest40196(path_param):
    path_value = path_param
    data = unquote(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
