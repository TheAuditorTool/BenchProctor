# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest50877():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
