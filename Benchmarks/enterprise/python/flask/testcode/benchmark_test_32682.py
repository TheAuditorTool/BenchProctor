# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest32682():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
