# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest55550(path_param):
    path_value = path_param
    data = to_text(path_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
