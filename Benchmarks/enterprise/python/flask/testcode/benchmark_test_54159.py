# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest54159(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
