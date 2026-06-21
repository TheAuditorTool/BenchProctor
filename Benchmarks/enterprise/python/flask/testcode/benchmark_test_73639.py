# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest73639(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
