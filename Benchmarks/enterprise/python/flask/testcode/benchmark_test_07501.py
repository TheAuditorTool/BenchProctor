# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest07501(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
