# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest45401(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
