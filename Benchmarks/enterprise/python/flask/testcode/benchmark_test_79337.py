# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79337():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
