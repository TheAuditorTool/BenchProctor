# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest04925():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    return jsonify({'error': 'An internal error occurred'}), 500
