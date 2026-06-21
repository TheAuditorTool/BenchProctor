# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest20325(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
