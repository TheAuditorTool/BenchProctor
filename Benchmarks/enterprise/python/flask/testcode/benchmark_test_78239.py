# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest78239(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
