# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from types import SimpleNamespace


def BenchmarkTest06402(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
