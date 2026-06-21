# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest62640():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
