# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest79851(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
