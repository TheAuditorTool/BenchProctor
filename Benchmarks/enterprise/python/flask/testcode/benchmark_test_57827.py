# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest57827(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
