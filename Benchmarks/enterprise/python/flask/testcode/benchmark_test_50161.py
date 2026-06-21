# SPDX-License-Identifier: Apache-2.0
import hashlib
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest50161():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
