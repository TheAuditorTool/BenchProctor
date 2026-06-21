# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75182():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
