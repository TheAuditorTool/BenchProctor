# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import importlib


def BenchmarkTest79034():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
