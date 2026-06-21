# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib


def BenchmarkTest64674():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
