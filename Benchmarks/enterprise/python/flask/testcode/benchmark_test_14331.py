# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest14331(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
