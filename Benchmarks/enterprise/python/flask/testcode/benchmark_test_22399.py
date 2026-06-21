# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22399():
    user_id = request.args.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
