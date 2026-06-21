# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest32569():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
