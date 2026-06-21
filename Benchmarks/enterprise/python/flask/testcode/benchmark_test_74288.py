# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest74288(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
