# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest12398(path_param):
    path_value = path_param
    data = to_text(path_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
