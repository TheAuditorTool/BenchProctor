# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest13215():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
