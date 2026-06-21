# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest74781(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
