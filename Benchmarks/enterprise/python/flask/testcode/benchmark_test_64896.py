# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest64896(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
