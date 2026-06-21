# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01332():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
