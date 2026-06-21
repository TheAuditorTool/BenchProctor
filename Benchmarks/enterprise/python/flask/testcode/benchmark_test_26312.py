# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest26312():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
