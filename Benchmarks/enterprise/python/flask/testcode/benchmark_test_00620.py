# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest00620(path_param):
    path_value = path_param
    data = f'{path_value}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
