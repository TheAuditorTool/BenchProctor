# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08952():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
