# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest23717(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
