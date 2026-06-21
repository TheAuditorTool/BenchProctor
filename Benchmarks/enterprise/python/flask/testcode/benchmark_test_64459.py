# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest64459(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
