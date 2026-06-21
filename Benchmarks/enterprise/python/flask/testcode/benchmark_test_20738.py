# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest20738(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
