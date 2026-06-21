# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest79165():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
