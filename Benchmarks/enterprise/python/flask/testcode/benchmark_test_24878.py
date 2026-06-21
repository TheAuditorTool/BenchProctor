# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest24878(path_param):
    path_value = path_param
    data = to_text(path_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
