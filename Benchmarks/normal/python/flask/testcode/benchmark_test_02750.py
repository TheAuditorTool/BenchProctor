# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02750(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
