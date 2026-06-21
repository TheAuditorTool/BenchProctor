# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
from types import SimpleNamespace


def BenchmarkTest74849():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
