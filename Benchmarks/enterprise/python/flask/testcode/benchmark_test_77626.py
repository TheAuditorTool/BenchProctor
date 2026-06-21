# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest77626(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
