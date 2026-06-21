# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55612():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
