# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest56727(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
