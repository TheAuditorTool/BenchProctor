# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest67611():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
