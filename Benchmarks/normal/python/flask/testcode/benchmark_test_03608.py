# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03608():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
