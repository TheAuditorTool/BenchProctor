# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest01263():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
