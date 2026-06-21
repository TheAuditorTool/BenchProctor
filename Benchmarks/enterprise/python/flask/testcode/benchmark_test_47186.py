# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest47186():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
