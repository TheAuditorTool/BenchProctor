# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest29046():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
