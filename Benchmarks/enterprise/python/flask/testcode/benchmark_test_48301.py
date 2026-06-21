# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest48301(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
