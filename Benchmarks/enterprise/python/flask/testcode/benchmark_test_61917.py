# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest61917():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
