# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest61544():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
