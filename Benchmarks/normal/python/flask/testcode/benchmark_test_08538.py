# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest08538(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
