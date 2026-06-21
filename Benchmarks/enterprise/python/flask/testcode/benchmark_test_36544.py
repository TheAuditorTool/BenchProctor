# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest36544():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
