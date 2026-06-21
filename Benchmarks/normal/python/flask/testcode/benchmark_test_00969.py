# SPDX-License-Identifier: Apache-2.0
import random
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest00969(path_param):
    path_value = path_param
    data = unquote(path_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
