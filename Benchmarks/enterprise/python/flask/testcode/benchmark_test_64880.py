# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest64880():
    referer_value = request.headers.get('Referer', '')
    digest = hashlib.sha256(str(referer_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
