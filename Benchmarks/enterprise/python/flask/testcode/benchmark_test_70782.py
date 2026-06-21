# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest70782(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
