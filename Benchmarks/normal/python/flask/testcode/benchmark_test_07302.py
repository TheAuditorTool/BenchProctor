# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest07302(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
