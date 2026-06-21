# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05246():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
