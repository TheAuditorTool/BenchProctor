# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest19818():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
