# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest71592():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
