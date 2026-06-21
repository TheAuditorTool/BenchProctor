# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest50775():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
