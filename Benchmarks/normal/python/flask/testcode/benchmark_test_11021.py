# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11021():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
