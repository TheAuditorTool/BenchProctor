# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest34313(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
