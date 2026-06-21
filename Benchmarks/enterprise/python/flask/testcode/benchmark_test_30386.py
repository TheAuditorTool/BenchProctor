# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest30386():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
