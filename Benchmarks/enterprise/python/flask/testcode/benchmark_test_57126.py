# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest57126(path_param):
    path_value = path_param
    with open('output.csv', 'a') as fh:
        fh.write(str(path_value) + ',data\n')
    return jsonify({"result": "success"})
