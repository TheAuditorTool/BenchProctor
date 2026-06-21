# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest07418(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
