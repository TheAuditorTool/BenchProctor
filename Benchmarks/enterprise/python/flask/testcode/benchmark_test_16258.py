# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest16258(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
