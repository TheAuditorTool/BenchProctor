# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest01718():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
