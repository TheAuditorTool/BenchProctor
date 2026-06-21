# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest40286():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
