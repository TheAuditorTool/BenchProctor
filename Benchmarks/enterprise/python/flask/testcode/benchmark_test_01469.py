# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest01469(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
