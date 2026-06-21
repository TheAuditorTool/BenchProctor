# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest20640(path_param):
    path_value = path_param
    if path_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    eval(str(processed))
    return jsonify({"result": "success"})
