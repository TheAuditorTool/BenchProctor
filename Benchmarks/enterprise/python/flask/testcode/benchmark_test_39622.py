# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest39622():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
