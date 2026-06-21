# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest69455():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
