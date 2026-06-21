# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest44104(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
