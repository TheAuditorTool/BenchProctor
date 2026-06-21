# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest39331(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    processed = data[:64]
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
