# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01131(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
