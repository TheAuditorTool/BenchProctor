# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest16105():
    user_id = request.args.get('id', '')
    digest = hashlib.md5(str(user_id).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
