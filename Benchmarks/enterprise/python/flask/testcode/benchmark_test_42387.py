# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42387():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
