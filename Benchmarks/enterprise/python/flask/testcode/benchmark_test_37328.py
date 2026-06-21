# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def to_text(value):
    return str(value).strip()

def BenchmarkTest37328():
    xml_value = request.get_data(as_text=True)
    data = to_text(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
