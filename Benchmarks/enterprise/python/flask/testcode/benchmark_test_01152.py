# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest01152():
    user_id = request.args.get('id', '')
    digest = str(user_id).encode().hex()
    return jsonify({'digest': str(digest)}), 200
