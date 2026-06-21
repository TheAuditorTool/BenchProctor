# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest73788(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
