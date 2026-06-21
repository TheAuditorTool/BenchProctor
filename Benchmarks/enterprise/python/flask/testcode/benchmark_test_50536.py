# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest50536(path_param):
    path_value = path_param
    random.seed(int(path_value) if str(path_value).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
