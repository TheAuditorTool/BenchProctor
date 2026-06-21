# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest00107():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
