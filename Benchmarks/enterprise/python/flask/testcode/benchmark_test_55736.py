# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest55736():
    user_id = request.args.get('id', '')
    digest = hashlib.sha1(str(user_id).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
