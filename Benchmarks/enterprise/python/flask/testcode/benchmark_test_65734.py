# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest65734():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
