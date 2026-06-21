# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest15506(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
