# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest42785():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
