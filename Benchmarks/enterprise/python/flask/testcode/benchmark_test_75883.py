# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest75883(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
