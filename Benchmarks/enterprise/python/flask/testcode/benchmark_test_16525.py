# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest16525():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
