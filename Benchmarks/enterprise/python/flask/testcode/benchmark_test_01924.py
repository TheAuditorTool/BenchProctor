# SPDX-License-Identifier: Apache-2.0
import hashlib
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest01924():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
