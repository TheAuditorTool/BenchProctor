# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest13554(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
