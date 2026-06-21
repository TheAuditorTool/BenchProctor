# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest26265():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    return jsonify({'error': 'An internal error occurred'}), 500
