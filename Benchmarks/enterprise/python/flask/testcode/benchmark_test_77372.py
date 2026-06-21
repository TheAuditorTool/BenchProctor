# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest77372():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
