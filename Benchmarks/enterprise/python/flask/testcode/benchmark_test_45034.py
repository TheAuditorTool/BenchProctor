# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest45034():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
