# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest60067():
    user_id = request.args.get('id', '')
    digest = hashlib.sha256(('static_salt_123' + str(user_id)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
