# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest34468():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
