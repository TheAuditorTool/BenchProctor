# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
import re


def BenchmarkTest12906():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
